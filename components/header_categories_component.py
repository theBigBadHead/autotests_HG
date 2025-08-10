from typing import List, Pattern
import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button
from elements.link import Link
from elements.text import Text
from elements.image import Image


class HeaderCategoriesComponent(BaseComponent):
    """
    Компонент меню категорий в хедере сайта HappyGifts.
    Содержит методы для открытия меню, получения списка категорий,
    проверки их отображения и перехода в выбранную категорию.
    Ожидает наличие атрибутов:
      - header-catalog-button
      - header-categories-mega-menu
      - header-category-item (повторяющийся)
      - header-category-icon
    """

    def __init__(self, page: Page):
        """
        Инициализирует элемент категорий.

        :param page: Экземпляр Playwright Page
        """

        super().__init__(page)
        # атомарные элементы из PageFactory
        #self.catalog_button = Button(page, "header-catalog-button", "Catalog button")
        self.catalog_button = Button(
            page=page,
            locator='//button[contains(text(),"Каталог")]',
            name='Кнопка "Каталог"'
        )

        #self.mega_menu = Text(page, "header-categories-mega-menu", "Mega menu container")
        self.menu_container = Text(
            page=page,
            locator='//nav[contains(@class,"NavigationMenu")]',
            name='Контейнер категорий в меню'
        )
        # повторяющийся элемент для ссылок категорий (data-testid="header-category-item")

        #self.category_link = Link(page, "header-category-item", "Header category link")
        self.category_link = Link(
            page=page,
            locator='//nav[contains(@class,"NavigationMenu")]//a[contains(@class,"MenuLink")]',
            name='Ссылка категории в меню'
        )

        # иконка категории (если нужна проверка изображений) - неявные
        #self.category_icon = Image(page, "header-category-icon", "Category icon")
        # self.category_icon = Image(
        #     page=page,
        #     locator='header-category-icon',
        #     name='Иконка категории'
        # )

    @allure.step("Open categories menu")
    def open(self) -> None:
        """
        Открывает (открытие/раскрытие) меню категорий в хедере.
        Использует click на кнопке каталога и ждёт появления контейнера мегаменю.
        """
        self.catalog_button.click()
        self.menu_container.check_visible()

    @allure.step("Get visible categories list")
    def list_categories(self) -> List[str]:
        """
        Возвращает список видимых названий категорий в мегаменю.
        :return: Список строк
        """
        self.open()
        items = self.page.get_by_test_id("header-category-item")
        count = items.count()
        return [items.nth(i).inner_text().strip() for i in range(count)]

    @allure.step("Check visible categories: {expected_categories}")
    def check_visible_categories(self, expected_categories: List[str]) -> None:
        """
        Проверяет, что все ожидаемые категории присутствуют в меню.
        :param expected_categories: Список ожидаемых названий категорий
        """
        actual = self.list_categories()
        for cat in expected_categories:
            assert cat in actual, f"Категория '{cat}' отсутствует в меню. Найдено: {actual}"

    @allure.step("Select category by name: {name}")
    def select_category(self, name: str) -> None:
        """
        Находит и кликает категорию, по-видимому, тексту внутри повторяющихся элементов.
        :param name: Название категории (точное вхождение)
        """
        self.open()
        items = self.page.get_by_test_id("header-category-item")
        # фильтрация по тексту внутри каждого элемента
        target = items.filter(has_text=name).first
        expect(target).to_be_visible()
        target.click()

    @allure.step("Select category and check URL")
    def select_category_and_check_url(self, name: str, expected_url_pattern: Pattern[str]) -> None:
        """
        Переходит в категорию и проверяет URL регулярным выражением.
        :param name: название категории
        :param expected_url_pattern: compiled regex для проверки URL (Pattern[str])
        """
        self.select_category(name)
        self.check_current_url(expected_url_pattern)

    @allure.step("Check category existence: {name}")
    def category_exists(self, name: str) -> bool:
        """
        Проверяет наличие заданной категории в списке.
        :param name: Название категории
        :return: True если найдена, иначе False
        """
        self.open()
        items = self.page.get_by_test_id("header-category-item")
        return items.filter(has_text=name).count() > 0

    @allure.step("Get categories count")
    def get_categories_count(self) -> int:
        """
        Возвращает количество элементов категорий в мегаменю.
        """
        self.open()
        items = self.page.get_by_test_id("header-category-item")
        return items.count()

    @allure.step("Check category icons are visible")
    def check_category_icons_visible(self) -> None:
        """
        Проверяет, что у каждой категории видна иконка (если у вас есть data-testid для иконок).
        """
        self.open()
        icons = self.page.get_by_test_id("header-category-icon")
        count = icons.count()
        for i in range(count):
            expect(icons.nth(i)).to_be_visible()