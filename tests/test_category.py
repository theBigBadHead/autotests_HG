import re
import allure
import pytest
from playwright.sync_api import expect

from pages.main_page import MainPage
from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.ui
class TestCategories:
    @allure.title("Проверка наличия всех категорий и коллекций")
    def test_check_category_and_collections(self, main_page: MainPage):
        main_page.visit(AppRoute.ROOT)
        main_page.header_categories_component.open()
        main_page.header_categories_component.check_all_categories()
        main_page.header_categories_component.check_all_collections()