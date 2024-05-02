from .api_object import ApiObject

"""
Рекомендации Маркета, касающиеся цен
"""


class StatePrices(ApiObject):

    class Price(ApiObject):
        value: float = None
        currencyId: str = None

        def __init__(self, data):
            super().__init__(data)

    class CofinancePrice(ApiObject):
        value: float = None
        currencyId: str = None
        updatedAt: str = None

        def __init__(self, data):
            super().__init__(data)

    offerId: str = None
    """Цена товара в каталоге."""
    price: Price = None
    """Заданная цена для участия в софинансировании скидок."""
    cofinancePrice: CofinancePrice = None
    """Привлекательность цены товара."""
    competitiveness: str = None
    """Количество показов карточки товара за последние 7 дней."""
    shows: int = None

    def __init__(self, data):
        super().__init__(data)
