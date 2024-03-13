from .api_object import ApiObject


class Product(ApiObject):

    class BasicPrice(ApiObject):

        value: float = None
        currencyId: str = None
        discountBase: float = None
        updatedAt: str = None

        def __init__(self, data):
            super().__init__(data)

    class DefaultPrice(ApiObject):

        value: float = None
        currencyId: str = None
        updatedAt: str = None

        def __init__(self, data):
            super().__init__(data)

    class Campaign(ApiObject):

        campaignId: int = None
        status: str = None

    offerId: str = None
    name: str = None
    category: str = None
    pictures: list[str] = None
    barcodes: list[str] = None
    description: str = None
    basicPrice: BasicPrice = None
    purchasePrice: DefaultPrice = None
    additionalExpenses: DefaultPrice = None
    cofinancePrice: DefaultPrice = None
    cardStatus: str = None
    campaigns: list[Campaign] = None
    marketSku = None

    def __init__(self, data):
        super().__init__(data)


if __name__ == '__main__':
    pass
