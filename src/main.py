from .config import BUISNESS_LOGO, GREEN_TEXT
from .eula import eula_accept
from .parser_module import parser_module_init, main_parser


def main():
    print(BUISNESS_LOGO)
    exit(1) if not eula_accept() else ...

    print(GREEN_TEXT.format(text='Eula accepted'))
    DRIVER, COURSE_ID, GROUP_ID, COOKIES = parser_module_init()
    main_parser(DRIVER, COURSE_ID, GROUP_ID)


if __name__ == '__main__':
    main()
