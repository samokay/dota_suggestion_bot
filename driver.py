import traceback

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Driver:
    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--headless")
            cls.__instance = webdriver.Chrome(
                ChromeDriverManager().install(), options=chrome_options
            )
        return cls.__instance
