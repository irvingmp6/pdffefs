from pathlib import Path

acceptable_list = ['jpg', 'jpeg']

def make_linux_friendly(input_path):
    path = Path(input_path)
    linux_path = str(path.absolute()).replace("\\","/")

    msg = (f"File was not found:\n{linux_path}")
    if not path.is_file():
        raise FileNotFoundError(msg)

    if path.suffix.lower() == "pdf":
        msg = (f"File extenstion is not pdf:\n{linux_path}")
        raise WrongFileExtension(msg)

    return linux_path


def pathlib_path(input_path):
    msg = (f"File was not found:\n{input_path}")
    path = Path(input_path)
    if not path.is_file():
        raise FileNotFoundError(msg)
    return input_path


class WrongFileExtension(Exception):
    """"Custom exception"""