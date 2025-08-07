from elements.base_element import BaseElement


class Text(BaseElement):
    """
    Класс для работы с текстовыми элементами на странице.
    Наследует все основные методы от BaseElement, предоставляя возможность
    работать с текстом как элементом на странице.
    """

    @property
    def type_of(self) -> str:
        """
        Возвращает тип элемента. В случае текста возвращается "text".
        """
        return "text"