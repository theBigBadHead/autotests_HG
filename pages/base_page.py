from typing import Pattern

import allure
from playwright.sync_api import Page, expect

from tools.logger import get_logger

logger = get_logger("BASE_PAGE")


class BasePage:
    """
    Базовый класс для всех PageObject-страниц.

    Содержит общие действия:
    - переход по URL
    - перезагрузка страницы
    - проверка текущего URL
    """

    def __init__(self, page: Page):
        """
        :param page: Экземпляр страницы Playwright
        """
        self.page = page

    def visit(self, url: str):
        """
        Открывает страницу по-заданному URL и ждёт полной загрузки.

        :param url: URL страницы
        """
        step = f'Opening the url "{url}"'

        with allure.step(step):
            logger.info(step)
            # Переход на указанный URL
            self.page.goto(url, wait_until='networkidle')

    def reload(self):
        """
        Перезагружает текущую страницу и ждёт загрузки DOM.
        """
        step = f'Reloading page with url "{self.page.url}"'

        with allure.step(step):
            logger.info(step)
            # Перезагрузка страницы
            self.page.reload(wait_until='domcontentloaded')

    def check_current_url(self, expected_url: Pattern[str]):
        """
        Проверяет, что текущий URL соответствует ожидаемому регулярному выражению.

        :param expected_url: Ожидаемый URL как регулярное выражение (Pattern)
        """
        step = f'Checking that current url matches pattern "{expected_url.pattern}"'

        with allure.step(step):
            logger.info(step)
            # Проверка соответствия текущего URL
            expect(self.page).to_have_url(expected_url)