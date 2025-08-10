import re

from playwright.sync_api import Page

from pages.base_page import BasePage
from components.header_categories_component import HeaderCategoriesComponent


class MainPage(BasePage):
    """
    Главная страница (MainPage).

    Включает элементы:
    - Шапка сайта

    Наследуется от BasePage.
    """

    def __init__(self, page: Page):
        """
        Инициализация главной страницы.

        :param page: Экземпляр страницы Playwright
        """
        super().__init__(page)

        self.header_categories_component = HeaderCategoriesComponent(page=page)
