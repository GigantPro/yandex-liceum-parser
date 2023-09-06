from .config import BUISNESS_LOGO
from .eula import eula_accept
from .parser_module import parser_module_init


def main():
    print(BUISNESS_LOGO)
    exit(1) if not eula_accept() else ...

    parser_module_init()


if __name__ == '__main__':
    main()
