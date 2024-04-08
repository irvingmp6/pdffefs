def get_help_menu() -> dict:
    menu = {}
    menu['desc'] = """Utilities to work with PDFs"""
    menu['subparsers'] = """"""

    menu['merge'] = {}
    menu['merge']['desc'] = """Merge list of PDF files into a single PDF file"""
    menu['merge']['pdf_files'] = """List of PDF file paths"""
    menu['merge']['output'] = """Filepath of output PDF. Defaults to './merged.pdf'"""

    menu['split'] = {}
    menu['split']['desc'] = """Split PDF file into list of PDF files"""
    menu['split']['pdf_file'] = """PDF file path to split"""
    menu['split']['output'] = """Directory to place PDFs. Defaults to current directory.'"""

    menu['convert'] = {}
    menu['convert']['desc'] = """Converts file into PDF"""
    menu['convert']['file_to_convert'] = """Paths of file to convert. Types allowed: JPG, JPEG"""
    menu['convert']['output'] = """Directory to place PDFs. Defaults to current directory.'"""

    return menu
