import os
import argparse
import textwrap

from PyPDF4 import PdfFileReader, PdfFileWriter, PdfFileMerger
from PIL import Image

from _version import __version__
from src.interface.interface_text import get_help_menu
from src.interface.interface_funcs import check_path
from src.interface.interface_funcs import WrongFileExtension


def merge_pdfs(args: argparse.Namespace) -> None:
    """
    Merge multiple PDF files into one.

    Args:
        args: Arguments parsed from the command line.
    """
    pdfs = args.pdf_files
    output = args.output

    # Create default file path
    if os.path.isdir(output):
        output = os.path.join(output, 'merged.pdf')

    # Create merger object
    merger = PdfFileMerger()

    # Iterate through PDF files and append them to the merger
    for pdf in pdfs:
        try:
            merger.append(check_path(pdf, "pdf"))
        except (WrongFileExtension, FileNotFoundError) as e:
            print(f"Skpping file: {e}")

    # Write file and close 
    merger.write(output)
    merger.close()

def split_pdfs(args: argparse.Namespace) -> None:
    """
    Split a PDF file into multiple files.

    Args:
        args: Arguments parsed from the command line.
    """
    pdf_file = args.pdf_file
    output_dir = args.output

    # Create output directory if doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create reader object
    pdf_reader = PdfFileReader(open(pdf_file, "rb"))

    # Iterate through PDF pages and create a separate file for each page
    for i, page in enumerate(pdf_reader.pages):
        count = i+1
        output = PdfFileWriter()
        output.addPage(page)
        file_name = f"{os.path.split(pdf_file)[1][:-4]}_{count}.pdf"
        out_file_path = os.path.join(output_dir, file_name)
        with open(out_file_path, "wb") as output_stream:
            output.write(output_stream)

def convert_to_pdf(args: argparse.Namespace) -> None:
    """
    Convert image files (JPG/JPEG) to PDF.

    Args:
        args: Arguments parsed from the command line.
    """
    output = args.output
    files = args.files_to_convert

    # Create output directory if doesn't exist
    if not os.path.isdir(output):
        os.mkdir(output)

    # Iterate through list of files to convert to PDF
    for file in files:

        # Check for file type compatibility
        extension = os.path.split(file)[1].split('.')[1].upper()
        if extension in ('JPG', 'JPEG'):
            image = Image.open(file)
            pdf_path = os.path.join(output, os.path.split(file)[1]) + ".pdf"
            image.save(pdf_path, "PDF", resolution=100.0, save_all=True)

        # Inform message user type isn't supported
        else:
            print(f"Could not convert: {file}\nThat file type is not supported.")

def get_args() -> argparse.Namespace:
    """
    Parse command line arguments.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    menu = get_help_menu()
    cli = argparse.ArgumentParser(
        prog='pdffefs',  # Program name
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(menu['desc'])
    )
    subparsers = cli.add_subparsers(help=menu['subparsers'])

    # Merge command parser
    merge_parser = subparsers.add_parser('merge', help=menu['merge']['desc'])
    merge_parser.add_argument('pdf_files', nargs='+', help=menu['merge']['pdf_files'])
    merge_parser.add_argument('--output', '-o', default='merged.pdf', help=menu['merge']['output'])
    merge_parser.set_defaults(func=merge_pdfs)

    # Split command parser
    split_parser = subparsers.add_parser('split', help=menu['split']['desc'])
    split_parser.add_argument('pdf_file', help=menu['split']['pdf_file'])
    split_parser.add_argument('--output', '-o', default='.', help=menu['split']['output'])
    split_parser.set_defaults(func=split_pdfs)

    # Convert command parser
    convert_parser = subparsers.add_parser('convert', help=menu['convert']['desc'])
    convert_parser.add_argument('files_to_convert', nargs='+', help=menu['convert']['file_to_convert'])
    convert_parser.add_argument('--output', '-o', default='.', help=menu['convert']['output'])
    convert_parser.set_defaults(func=convert_to_pdf)

    return cli.parse_args()

def main():
    """
    Main function to parse command line arguments and execute corresponding functions.
    """
    args = get_args()
    if hasattr(args, "func"):
        args.func(args)

if __name__ == "__main__":
    main()