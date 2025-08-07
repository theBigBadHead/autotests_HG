import allure
from playwright.sync_api import Page, Locator, expect

from tools.logger import get_logger

logger = get_logger("BASE_ELEMENT")


class BaseElement:
    """
    Базовый элемент страницы.

    Предоставляет общие методы взаимодействия с любым UI-элементом,
    включая клик, проверку видимости, проверку текста и получение локатора.
    """
    def __init__(self, page: Page, locator: str, name: str) -> None:
        """
        :param page: Экземпляр страницы Playwright
        :param locator: Значение data-testid для поиска элемента (может содержать плейсхолдеры)
        :param name: Название элемента (для логирования и аллюра)
        """
        self.page = page
        self.name = name
        self.locator = locator

    @property
    def type_of(self) -> str:
        """
        Возвращает тип элемента. Переопределяется в потомках.
        """
        return "base element"

    def get_locator_by_test_id(self, nth: int = 0, **kwargs) -> Locator:
        """
        Формирует локатор элемента по data-testid с возможностью подстановки аргументов.

        :param nth: Индекс элемента, если на странице несколько одинаковых
        :param kwargs: Аргументы для форматирования локатора
        :return: Локатор элемента
        """
        locator = self.locator.format(**kwargs)
        step = f'Getting locator with "data-testid={locator}" at index "{nth}"'

        with allure.step(step):
            logger.info(step)
            return self.page.get_by_test_id(locator).nth(nth)

    def get_locator_by_xpath(self, nth: int = 0, **kwargs) -> Locator:
        """
        Формирует локатор по XPath с возможностью подстановки аргументов и выбором элемента по индексу.

        :param nth: Индекс элемента, если на странице несколько одинаковых
        :param kwargs: Аргументы для подстановки в XPath-шаблон
        :return: Локатор элемента
        """
        xpath = self.locator.format(**kwargs)
        step = f'Getting locator by XPath: {xpath} at index "{nth}"'

        with allure.step(step):
            logger.info(step)
            return self.page.locator(f'xpath={xpath}').nth(nth)

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        """
        Определяет тип локатора (data-testid или XPath) и возвращает соответствующий Locator.

        :param nth: Индекс элемента
        :param kwargs: Аргументы для форматирования
        :return: Locator
        """
        if self.locator.strip().startswith('//') or 'xpath=' in self.locator:
            return self.get_locator_by_xpath(nth=nth, **kwargs)
        else:
            return self.get_locator_by_test_id(nth=nth, **kwargs)

    def click(self, nth: int = 0, **kwargs):
        """
        Выполняет клик по элементу.

        :param nth: Индекс элемента (по умолчанию 0)
        :param kwargs: Аргументы для форматирования локатора
        """
        step = f'Clicking {self.type_of} "{self.name}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.click()

    def check_visible(self, nth: int = 0, **kwargs):
        """
        Проверяет, что элемент видим на странице.

        :param nth: Индекс элемента
        :param kwargs: Аргументы для форматирования локатора
        """
        step = f'Checking that {self.type_of} "{self.name}" is visible'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        """
        Проверяет, что у элемента присутствует заданный текст.

        :param text: Ожидаемый текст
        :param nth: Индекс элемента
        :param kwargs: Аргументы для форматирования локатора
        """
        step = f'Checking that {self.type_of} "{self.name}" has text "{text}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_text(text)