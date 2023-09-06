from .get_cookies import get_cookies


DRIVER = None

def parser_module_init() -> None:
    global DRIVER

    DRIVER = get_cookies()
