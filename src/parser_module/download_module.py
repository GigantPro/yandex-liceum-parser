from os import makedirs
from pathlib import Path
import asyncio

import aiofiles
import aiohttp

from ..config import BLUE_TEXT, GREEN_TEXT, RED_TEXT


__all__ = ("download_answers",)

def prepearing_answers(path_to_save: Path, data_to_download: list[tuple[str, str, str]]) -> None:
    print(BLUE_TEXT.format(text='Prepearing answers paths...'), end='')
    for lesson_title, *_ in data_to_download:
        path_to_save_lesson = path_to_save.joinpath(lesson_title)
        makedirs(path_to_save_lesson, exist_ok=True)
    print(GREEN_TEXT.format(text='ok'))


def download_answers(path_to_save: Path, data_to_download: list[tuple[str, str, str]]) -> None:
    prepearing_answers(path_to_save, data_to_download)
    asyncio.run(download_files_controller(path_to_save, data_to_download))


async def download_files_controller(path_to_save: Path, data_to_download: list[tuple[str, str, str]]) -> None:
    print(GREEN_TEXT.format(text='The replies of the answers have begun'))
    
    queue = asyncio.Queue()
    for lesson_title, task_title, file in data_to_download:
        queue.put_nowait(
            (
                path_to_save.joinpath(lesson_title).joinpath(task_title),
                file,
            )
        )
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[download_file_worker(queue, session) for _ in range(100)])


async def download_file_worker(queue: asyncio.Queue, session: aiohttp.ClientSession) -> None:
    while True:
        try:
            task_path, url = queue.get_nowait()
            async with session.get(url) as response:
                if response.status != 200:
                    print(RED_TEXT.format(text=f'Failed to download {url}'))
                data = await response.read()
                async with aiofiles.open(f"{task_path}.{url.split('.')[-1]}", 'wb') as file:
                    await file.write(data)

                queue.task_done()
        except asyncio.QueueEmpty:
            return 
