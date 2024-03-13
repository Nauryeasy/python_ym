from .api_object import ApiObject


class OrderData(ApiObject):

    class DeliveryRegion(ApiObject):
        id: int = None
        name: str = None

    class Commission(ApiObject):
        type: str = None
        actual: float = None

    class ItemOfOrder(ApiObject):

        class WareHouse(ApiObject):

            id: int = None
            name: str = None

            def __init__(self, data):
                super().__init__(data)

        offerName: str = None
        marketSku: int = None
        shopSku: str = None
        count: int = None
        prices: list = None
        warehouse: WareHouse = None
        bidFee: float = None
        cofinanceThreshold: float = None
        cofinanceValue: float = None

        # Not Receivable via API
        price_total: float = None

        def __init__(self, data):
            super().__init__(data)

            for price in self.prices:
                if price['type'] == 'BUYER':
                    self.price_total = price['total']

            self.prices = None

    id: int = None
    status: str = None
    partnerOrderId: str = None
    items: list[ItemOfOrder] = None
    commissions: list[Commission] = None
    deliveryRegion: DeliveryRegion = None

    def __init__(self, data):
        super().__init__(data)


if __name__ == '__main__':
    pass
