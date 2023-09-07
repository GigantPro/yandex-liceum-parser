from .get_cookies import get_cookies
from .main_parser import main_parser
from .download_module import download_answers


def parser_module_init():
    DRIVER, COOKIES = get_cookies()

    print('Url template: https://lms.yandex.ru/courses/{COURSE_ID}/groups/{GROUP_ID}')
    COURSE_ID = int(input('Course ID: '))
    GROUP_ID  = int(input('Group ID: '))
    
    return DRIVER, COURSE_ID, GROUP_ID, COOKIES
