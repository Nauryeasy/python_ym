from .api_object import ApiObject

"""
Рекомендации Маркета, касающиеся цен
"""


class RecommendationPrices(ApiObject):

    class CompetitivenessThresholds(ApiObject):

        class RecommendedCofinancePrice(ApiObject):
            value: float = None
            currencyId: str = None

            def __init__(self, data):
                super().__init__(data)

        """Максимальная привлекательная цена."""
        optimalPrice: RecommendedCofinancePrice = None
        """Максимальная умеренная цена."""
        averagePrice: RecommendedCofinancePrice = None

        def __init__(self, data):
            super().__init__(data)

    offerId: str = None
    """Рекомендованное значение цены для участия в софинансировании скидки."""
    recommendedCofinancePrice: CompetitivenessThresholds.RecommendedCofinancePrice = None
    """Максимальные значения цены, при которых она является привлекательной или умеренной."""
    competitivenessThresholds: CompetitivenessThresholds = None

    def __init__(self, data):
        super().__init__(data)
