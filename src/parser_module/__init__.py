from .get_cookies import get_cookies


DRIVER      = None

COURSE_ID   = None
GROUP_ID    = None


def parser_module_init() -> None:
    global DRIVER, COURSE_ID, GROUP_ID

    DRIVER = get_cookies()

    print('Url template: https://lms.yandex.ru/courses/{COURSE_ID}/groups/{GROUP_ID}')
    COURSE_ID = int(input('Course ID: '))
    GROUP_ID  = int(input('Group ID: '))
