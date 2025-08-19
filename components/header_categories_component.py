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
      - catalog_button
      - categories_title
      - collections_title
      - links categories
      - links collections
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
            name='Промо-одежда',
        )
        self.umbrellas_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[2]/div/div[1]/a',
            name='Зонты',
        )
        self.bags_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[3]/div/div[1]/a',
            name='Сумки и рюкзаки',
        )
        self.dishes_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[4]/div/div[1]/a',
            name='Посуда'
        )
        self.gift_wrap_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[5]/div/a',
            name='Упаковка подарочная',
        )
        self.stationery_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[6]/div/div[1]/a',
            name='Ручки, карандаши и канцтовары',
        )
        self.travel_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[7]/div/div[1]/a',
            name='Путешествие и отдых',
        )
        self.home_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[8]/div/div[1]/a',
            name='Уютный дом',
        )
        self.office_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[9]/div/div[1]/a',
            name='Деловые и офисные аксессуары',
        )
        self.awards_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[10]/div/div[1]/a',
            name='Награды',
        )
        self.electronics_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[11]/div/div[1]/a',
            name='Электроника',
        )
        self.gift_sets_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[12]/div/a',
            name='Подарочные наборы',
        )
        self.promo_souvenirs_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[13]/div/div[1]/a',
            name='Промо-сувениры',
        )
        self.notebooks_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[14]/div/div[1]/a',
            name='Ежедневники и бизнес-блокноты',
        )
        self.raincoats_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[15]/div/a',
            name='Дождевики',
        )
        self.beauty_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[16]/div/a',
            name='Аксессуары для красоты',
        )
        self.health_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[17]/div/div[1]/a',
            name='Товары для здоровья',
        )
        self.aroma_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[18]/div/div[1]/a',
            name='Аромаподарки',
        )
        self.living_gifts_link = Link(
            page=page,
            locator='//*[@id="catalog"]/div/div[1]/ul/li[19]/div/div[1]/a',
            name='Живые подарки',
        )

        # --- Подборки ---
        self.hit_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4181"]/div/a',
            name='Хит',
        )
        self.new_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4182"]/div/a',
            name='Новинки',
        )
        self.custom_merch_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4358"]/div/a',
            name='Custom Merch',
        )
        self.atlantis_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4294"]/div/a',
            name='Конструктор бейсболок Atlantis',
        )
        self.new_year_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4183"]/div/a',
            name='Новый год',
        )
        self.men_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4185"]/div/a',
            name='Подарки для мужчин',
        )
        self.women_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4186"]/div/a',
            name='Подарки для женщин',
        )
        self.black_friday_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4187"]/div/a',
            name='BLACK FRIDAY',
        )
        self.warm_textile_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4188"]/div/a',
            name='Теплый текстиль',
        )
        self.sales_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4347"]/div/a',
            name='Sales ',
        )
        self.electronics_new_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4354"]/div/a',
            name='Электроника NEW',
        )
        self.soft_touch_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4191"]/div/a',
            name='Коллекция SOFT-TOUCH',
        )
        self.eco_life_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4192"]/div/a',
            name='ECO-LIFE',
        )
        self.safe_touch_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4193"]/div/a',
            name='SAFE TOUCH',
        )
        self.children_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4195"]/div/a',
            name='Подарки для детей',
        )
        self.reflective_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4201"]/div/a',
            name='Коллекция REFLECTIVE',
        )
        self.made_in_russia_link = Link(
            page=page,
            locator='//*[@id="bx_1847241719_4220"]/div/a',
            name='Сделано в России',
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
        self.catalog_button.check_enabled()
        self.catalog_button.click()

    @allure.step("Перейти в категорию")
    def go_to_category(self, link: Link):
        old_url = self.page.url
        self.categories_title.check_visible()
        link.check_visible()
        link.click()
        expect(self.page).not_to_have_url(old_url)

    @allure.step("Перейти в подборку {name}")
    def go_to_collection(self, link: Link):
        old_url = self.page.url
        self.collections_title.check_visible()
        link.check_visible()
        link.click()
        expect(self.page).not_to_have_url(old_url)

    @allure.step("Проверить все категории")
    def check_all_categories(self):
        self.categories_title.check_visible()
        for category in self.all_categories:
            category.check_visible()
            category.check_have_text(category.name)

    @allure.step("Проверить все подборки")
    def check_all_collections(self):
        self.collections_title.check_visible()
        for collection in self.all_collections:
            collection.check_visible()
            collection.check_have_text(collection.name)