import os
import argparse
import textwrap

from PyPDF4 import PdfFileReader
from PyPDF4 import PdfFileWriter
from PyPDF4 import PdfFileMerger
from PIL import Image

from _version import __version__

from src.interface.interface_text import get_help_menu
from src.interface.interface_funcs import make_linux_friendly

def merge_pdfs(args):
    pdfs = args.pdf_files
    output = args.output
    if os.path.isdir(output):
        output = os.path.join(output, 'merged.pdf')

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(make_linux_friendly(pdf))

    merger.write(output)
    merger.close()


def split_pdfs(args):
    pdf_file = args.pdf_file
    output_dir = args.output
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    pdf_reader = PdfFileReader(open(pdf_file, "rb"))
    out_paths = []
    for i, page in enumerate(pdf_reader.pages):
        count = i+1
        output = PdfFileWriter()
        output.addPage(page)
        file_name = f"{os.path.split(pdf_file)[1][:-4]}_{count}.pdf"
        out_file_path = os.path.join(output_dir, file_name)
        with open(out_file_path, "wb") as output_stream:
            output.write(output_stream)

        out_paths.append(out_file_path)

def convert_to_pdf(args):
    output = args.output
    files = args.files_to_convert
    if not os.path.isdir(output):
        os.mkdir(output)
    for file in files:
        extension = os.path.split(file)[1].split('.')[1].upper()
        if extension in ('JPG', 'JPEG'):
            image = Image.open(file)
            pdf_path = os.path.join(output, os.path.split(file)[1]) + ".pdf"
            image.save(pdf_path, "PDF" ,resolution=100.0, save_all=True)
        else:
            print(f"Could not convert: {file}\nThat file type is not supported.")

def get_args():
    menu = get_help_menu()
    cli = argparse.ArgumentParser(
        prog='pdffefs',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(menu['desc'])
    )
    subparsers = cli.add_subparsers(help=menu['subparsers'])

    merge_parser = subparsers.add_parser('merge', help=menu['merge']['desc'])
    merge_parser.add_argument('pdf_files', nargs='+', help=menu['merge']['pdf_files'])
    merge_parser.add_argument('--output', '-o', default='merged.pdf', help=menu['merge']['output'])
    merge_parser.set_defaults(func=merge_pdfs)

    split_parser = subparsers.add_parser('split', help=menu['split']['desc'])
    split_parser.add_argument('pdf_file', help=menu['split']['pdf_file'])
    split_parser.add_argument('--output', '-o', default='.', help=menu['split']['output'])
    split_parser.set_defaults(func=split_pdfs)

    convert_parser = subparsers.add_parser('convert', help=menu['convert']['desc'])
    convert_parser.add_argument('files_to_convert', nargs='+', help=menu['convert']['file_to_convert'])
    convert_parser.add_argument('--output', '-o', default='.', help=menu['convert']['output'])
    convert_parser.set_defaults(func=convert_to_pdf)

    return cli.parse_args()

def main():
    args = get_args()
    if hasattr(args, "func"):
        args.func(args)


if __name__ == "__main__":
    main()