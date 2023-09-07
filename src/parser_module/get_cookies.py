import pickle
from time import sleep

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from .config import COOKIES_PATH
from ..config import GREEN_TEXT, YELLOW_TEXT


def get_cookies() -> tuple[webdriver.Firefox, list[dict]]:
    if COOKIES_PATH.exists():
        print(GREEN_TEXT.format(text='Cookies already exist'))

        options = FirefoxOptions()
        options.headless = True
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

        driver.get('https://passport.yandex.ru')
        sleep(.5)
        cookies = pickle.load(open(COOKIES_PATH.absolute(), "rb"))
        for cookie in cookies:
            try:
                driver.add_cookie(cookie)
            except exceptions.InvalidCookieDomainException:
                ...

        return driver, cookies
    
    print(YELLOW_TEXT.format(text='The cookies are not found! The entrance in the window opened in the browser is required.'))
    options = FirefoxOptions()
    options.headless = False
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    driver.get('https://lms.yandex.ru')
    
    input(YELLOW_TEXT.format(text='As soon as you enter the entrance, click Enter'))
    
    pickle.dump(driver.get_cookies(), open(COOKIES_PATH.absolute(), "wb"))

    driver.quit()

    print(GREEN_TEXT.format(text='Cookies were saved'))

    options.headless = True
    return driver, driver.get_cookies()
