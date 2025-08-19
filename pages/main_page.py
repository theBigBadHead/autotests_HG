import re

from playwright.sync_api import Page

from pages.base_page import BasePage
from components.header_categories_component import HeaderCategoriesComponent
from elements.link import Link
from elements.button import Button


class MainPage(BasePage):
    """
    Главная страница (MainPage).

    Включает элементы:
    - Компонент HeaderCategoriesComponent для работы с каталогом.
    - Специфические элементы главной страницы.

    Наследуется от BasePage.
    """

    def __init__(self, page: Page):
        """
        Инициализация главной страницы.

        :param page: Экземпляр страницы Playwright
        """
        super().__init__(page)

        # Подключение компонента каталога из хедера
        self.header_categories_component = HeaderCategoriesComponent(page=page)

    def open_catalog(self):
        """
        Делегируем действие в компонент HeaderCategoriesComponent.
        """
        self.header_categories_component.open()
