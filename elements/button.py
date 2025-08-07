import allure
from playwright.sync_api import expect

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger("BUTTON")


class Button(BaseElement):
    """
    Класс для работы с кнопками на странице. Наследует базовые методы от BaseElement и добавляет
    специфичные методы для работы с кнопками, такие как проверка состояния (включена/выключена).
    """

    @property
    def type_of(self) -> str:
        """
        Возвращает тип элемента "button".
        Используется для унификации логирования и обработки элементов.
        """
        return "button"

    def check_enabled(self, nth: int = 0, **kwargs):
        """
        Проверяет, что кнопка активна (включена). Используется для тестирования сценариев,
        когда кнопка должна быть доступна для клика.

        :param nth: Индекс кнопки, если на странице несколько одинаковых элементов.
        :param kwargs: Дополнительные аргументы для локатора.
        :raises AssertionError: Если кнопка не активна.
        """
        step = f'Checking that {self.type_of} "{self.name}" is enabled'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_enabled()

    def check_disabled(self, nth: int = 0, **kwargs):
        """
        Проверяет, что кнопка не активна (выключена). Используется для тестирования сценариев,
        когда кнопка должна быть недоступна для клика.

        :param nth: Индекс кнопки, если на странице несколько одинаковых элементов.
        :param kwargs: Дополнительные аргументы для локатора.
        :raises AssertionError: Если кнопка активна.
        """
        step = f'Checking that {self.type_of} "{self.name}" is disabled'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_disabled()