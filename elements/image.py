from elements.base_element import BaseElement


class Image(BaseElement):
    """
    Класс для работы с изображениями на странице.
    Наследует все основные методы от BaseElement, предоставляя возможность
    работать с изображениями как элементами на странице.
    """

    @property
    def type_of(self) -> str:
        """
        Возвращает тип элемента. В случае изображения возвращается "image".
        """
        return "image"