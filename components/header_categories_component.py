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
        # Кнопка "Каталог" в хедере
        self.catalog_button = Button(
            page=page,
            locator='//*[@id="open-catalog"]',
            name='Кнопка "Каталог"'
        )
        # Заголовки секций
        self.categories_title = Text(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/a',
            name='Заголовок "Весь ассортимент"'
        )
        self.collections_title = Text(
            page=page,
            locator='//*[@id="catalog"]/div/div[2]/p',
            name='Заголовок "Коллекции и подборки"'
        )

        # --- Категории ---
        self.promo_clothes_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[1]/div/div[1]/a',
            name='Категория "Промо-одежда"',
        )
        self.umbrellas_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[2]/div/div[1]/a',
            name='Категория "Зонты"',
        )
        self.bags_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[3]/div/div[1]/a',
            name='Категория "Сумки и рюкзаки"',
        )
        self.dishes_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[4]/div/div[1]/a',
            name='Категория "Посуда"'
        )
        self.gift_wrap_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[5]/div/a',
            name='Категория "Упаковка подарочная"',
        )
        self.stationery_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[6]/div/div[1]/a',
            name='Категория "Ручки, карандаши и канцтовары"',
        )
        self.travel_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[7]/div/div[1]/a',
            name='Категория "Путешествие и отдых"',
        )
        self.home_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[8]/div/div[1]/a',
            name='Категория "Уютный дом"',
        )
        self.office_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[9]/div/div[1]/a',
            name='Категория "Деловые и офисные аксессуары"',
        )
        self.awards_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[10]/div/div[1]/a',
            name='Категория "Награды"',
        )
        self.electronics_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[11]/div/div[1]/a',
            name='Категория "Электроника"',
        )
        self.gift_sets_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[12]/div/a',
            name='Категория "Подарочные наборы"',
        )
        self.promo_souvenirs_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[13]/div/div[1]/a',
            name='Категория "Промо-сувениры"',
        )
        self.notebooks_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[14]/div/div[1]/a',
            name='Категория "Ежедневники и бизнес-блокноты"',
        )
        self.raincoats_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[15]/div/a',
            name='Категория "Дождевики"',
        )
        self.beauty_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[16]/div/a',
            name='Категория "Аксессуары для красоты"',
        )
        self.health_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[17]/div/div[1]/a',
            name='Категория "Товары для здоровья"',
        )
        self.aroma_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[18]/div/div[1]/a',
            name='Категория "Аромаподарки"',
        )
        self.living_gifts_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[19]/div/div[1]/a',
            name='Категория "Живые подарки"',
        )

        # --- Подборки ---
        self.hit_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4181"]/div/a',
            name='Подборка "Хит"',
        )
        self.new_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4182"]/div/a',
            name='Подборка "Новинки"',
        )
        self.custom_merch_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4358"]/div/a',
            name='Подборка "Custom Merch"',
        )
        self.atlantis_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4294"]/div/a',
            name='Подборка "Конструктор бейсболок Atlantis"',
        )
        self.new_year_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4183"]/div/a',
            name='Подборка "Новый год"',
        )
        self.men_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4185"]/div/a',
            name='Подборка "Подарки для мужчин"',
        )
        self.women_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4186"]/div/a',
            name='Подборка "Подарки для женщин"',
        )
        self.black_friday_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4187"]/div/a',
            name='Подборка "BLACK FRIDAY"',
        )
        self.warm_textile_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4188"]/div/a',
            name='Подборка "Теплый текстиль"',
        )
        self.sales_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4354"]/div/a',
            name='Подборка "Sales"',
        )
        self.electronics_new_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4354"]/div/a',
            name='Подборка "Электроника NEW"',
        )
        self.soft_touch_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4191"]/div/a',
            name='Подборка "Коллекция SOFT-TOUCH"',
        )
        self.eco_life_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4192"]/div/a',
            name='Подборка "ECO-LIFE"',
        )
        self.safe_touch_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4193"]/div/a',
            name='Подборка "SAFE TOUCH"',
        )
        self.children_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4195"]/div/a',
            name='Подборка "Подарки для детей"',
        )
        self.reflective_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4201"]/div/a',
            name='Подборка "Коллекция REFLECTIVE"',
        )
        self.made_in_russia_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4220"]/div/a',
            name='Подборка "Сделано в России"',
        )

        # Списки для удобной итерации
        self.all_categories = [
            self.promo_clothes_link,
            self.umbrellas_link,
            self.bags_link,
            self.dishes_link,
            self.gift_wrap_link,
            self.stationery_link,
            self.travel_link,
            self.home_link,
            self.office_link,
            self.awards_link,
            self.electronics_link,
            self.gift_sets_link,
            self.promo_souvenirs_link,
            self.notebooks_link,
            self.raincoats_link,
            self.beauty_link,
            self.health_link,
            self.aroma_link,
            self.living_gifts_link
        ]

        self.all_collections = [
            self.hit_link,
            self.new_link,
            self.custom_merch_link,
            self.atlantis_link,
            self.new_year_link,
            self.men_link,
            self.women_link,
            self.black_friday_link,
            self.warm_textile_link,
            self.sales_link,
            self.electronics_new_link,
            self.soft_touch_link,
            self.eco_life_link,
            self.safe_touch_link,
            self.children_link,
            self.reflective_link,
            self.made_in_russia_link
        ]

    @allure.step("Открыть меню каталога")
    def open(self):
        self.catalog_button.click()
        self.categories_title.check_visible()
        self.collections_title.check_visible()

    @allure.step("Перейти в категорию {name}")
    def go_to_category(self, link: Link):
        link.click()
        expect(self.page).to_have_url(lambda url: url != "")

    @allure.step("Перейти в подборку {name}")
    def go_to_collection(self, link: Link):
        link.click()
        expect(self.page).to_have_url(lambda url: url != "")

    @allure.step("Проверить все категории")
    def check_all_categories(self):
        for category in self.all_categories:
            category.check_visible()

    @allure.step("Проверить все подборки")
    def check_all_collections(self):
        for collection in self.all_collections:
            collection.check_visible()