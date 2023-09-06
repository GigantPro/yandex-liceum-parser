from .config import EULA_TEXT


def eula_accept() -> bool:
    print(EULA_TEXT)
    return True if input('Accept? [Y/n]: ').lower() == 'y' else False
