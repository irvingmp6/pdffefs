from pathlib import Path

acceptable_list = ['jpg', 'jpeg']

def check_path(input_path: str, extension: str) -> str:
    """
    Checks that path exists and is correct extension

    Args:
        input_path: (string) the path to be validated
        extension: (string) the expected extension
    """
    path = Path(input_path)

    msg = (f"File was not found: {input_path}")
    if not path.is_file():
        raise FileNotFoundError(msg)

    if path.suffix.lower() != extension.lower():
        msg = (f"File extenstion is not pdf: {input_path}")
        raise WrongFileExtension(msg)

    return input_path

class WrongFileExtension(Exception):
    """"Custom exception"""