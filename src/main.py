from .config import BUISNESS_LOGO, GREEN_TEXT
from .eula import eula_accept
from .parser_module import parser_module_init


def main():
    print(BUISNESS_LOGO)
    exit(1) if not eula_accept() else ...

    print(GREEN_TEXT.format(text='Eula accepted'))
    parser_module_init()


if __name__ == '__main__':
    main()
