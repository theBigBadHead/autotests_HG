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
    - Шапка сайта

    Наследуется от BasePage.
    """

    def __init__(self, page: Page):
        """
        Инициализация главной страницы.

        :param page: Экземпляр страницы Playwright
        """
        super().__init__(page)

        # Компоненты страницы
        self.header_categories_component = HeaderCategoriesComponent(page=page)

        # Элементы страницы
        self.categories_button = Button(
            page=page,
            name="Categories",
            locator='//*[@id="open-catalog"]') #Кнопка каталога
        self.promo_odezhda_link = Link(
            page=page,
            name="promo_odezhda",
            locator='//*[@id="catalog"]/div/div[1]/ul/li[1]/div/div[1]') #Промо-одежда
        self.first_product_link = Link(
            page=page,
            name="first_product",
            locator='//*[@id="component_search-results"]/div/div[1]'
        )

    def click_categories_button(self):
        """
        Клик на кнопку "Категории".

        :raises AssertionError: Если URL не соответствует ожидаемому
        """
        self.categories_button.click()

    def click_promo_odezhda_link(self):
        """
        Клик на ссылку "Промо-одежда".
        """
        self.promo_odezhda_link.click()
        self.check_current_url(re.compile(".*/catalog/promo_odezhda/"))

    def open_first_product(self):
        """
        Открытие первого товара из каталога и проверка, что он видим.
        """
        self.first_product_link.check_visible()
        self.first_product_link.click()
        self.check_current_url(re.compile(r".*/catalog/promo_odezhda/.*"))
