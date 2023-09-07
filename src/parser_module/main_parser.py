from json import loads
from os import makedirs
from pathlib import Path

from selenium.webdriver.common.by import By

from .download_module import download_answers
from ..config import GREEN_TEXT, BLUE_TEXT, YELLOW_TEXT


def main_parser(driver, COURSE_ID, GROUP_ID) -> None:
    print(GREEN_TEXT.format(text='Parsing started'))

    driver.get(f'https://lms.yandex.ru/api/student/tasks?courseId={COURSE_ID}&groupId={GROUP_ID}')
    s_json = driver.find_element(By.ID, 'json').text
    tasks_json = loads(s_json)

    print(GREEN_TEXT.format(text=f'There are {tasks_json["count"]} tasks in total'))
    
    resolved_tasks = []
    for task in tasks_json['results']:
        if 'solution' in task and \
                task['solution'] and \
                task['solution']['status']['type'] == 'accepted':
            resolved_tasks.append(task)

    print(GREEN_TEXT.format(text=f'There are {len(resolved_tasks)} resolved tasks'))

    tasks_urls = []
    for resolved_task in resolved_tasks:
        soluion_url = f"https://lms.yandex.ru/api/student/solutions/{resolved_task['solution']['id']}"
        driver.get(soluion_url)
        s_json = driver.find_element(By.ID, 'json').text
        tasks_json = loads(s_json)
        if tasks_json['file']:
            tasks_urls.append((resolved_task['lesson']['title'], resolved_task['title'], tasks_json['file']['url']))
    print(GREEN_TEXT.format(text=f'{len(tasks_urls)} solutions were found'))

    path_to_save_course = Path(__file__).parents[2].absolute().joinpath('answers')
    makedirs(path_to_save_course, exist_ok=True)
    print(BLUE_TEXT.format(text=f'The answers will be saved to: {YELLOW_TEXT.format(text=path_to_save_course.absolute())}'))

    download_answers(path_to_save=path_to_save_course, data_to_download=tasks_urls)
