def get_help_menu() -> dict:
    """
    Returns help text as a dictionary

    args:
        none 
    """
    menu = {
        'desc': "Utilities to work with PDFs",
        'subparsers': "",
        'merge': {
            'desc': "Merge list of PDF files into a single PDF file",
            'pdf_files': "List of PDF file paths",
            'output': "Filepath of output PDF. Defaults to './merged.pdf'"
        },
        'split': {
            'desc': "Split PDF file into list of PDF files",
            'pdf_file': "PDF file path to split",
            'output': "Directory to place PDFs. Defaults to current directory."
        },
        'convert': {
            'desc': "Converts file into PDF",
            'file_to_convert': "Paths of file to convert. Types allowed: JPG, JPEG",
            'output': "Directory to place PDFs. Defaults to current directory."
        }
    }

    return menu
