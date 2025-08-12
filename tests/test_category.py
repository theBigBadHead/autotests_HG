import re
import allure
import pytest
from playwright.sync_api import expect

from pages.main_page import MainPage
from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.ui
class TestCategories:
    @allure.title("Проверка категории 'Промо-одежда' и открытие первой ссылки из категории")
    def test_check_category_and_open_first_link(self, main_page: MainPage):
        main_page.visit(AppRoute.ROOT)

        main_page.click_categories_button()
        main_page.click_promo_odezhda_link()
        main_page.open_first_product()