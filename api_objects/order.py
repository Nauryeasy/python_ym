from .api_object import ApiObject
import datetime


class Order(ApiObject):

    class Subsidie(ApiObject):

        type: str = None
        amount = None

        def __init__(self, data):
            super().__init__(data)

    class ItemOfOrder(ApiObject):

        id: int = None
        offerId = None
        offerName = None
        price = None
        priceBeforeDiscount = None
        count = None
        vat = None
        partnerWarehouseId = None

        def __init__(self, data):
            super().__init__(data)

    id: int = None
    status: str = None
    substatus: str = None
    creationDate = None
    currency: str = None
    itemsTotal = None
    deliveryTotal = None
    items: list[ItemOfOrder] = None
    subsidies: list[Subsidie] = None

    # Not Receivable via API
    total: float = None
    subsidyTotal: float = None
    totalWithSubsidy: float = None

    def __init__(self, data):
        super().__init__(data)

        self.creationDate = datetime.datetime.strptime(self.creationDate, '%d-%m-%Y %H:%M:%S')
        self.creationDate = self.creationDate - datetime.timedelta(hours=3)

        self.subsidyTotal = sum(subsidy.amount for subsidy in self.subsidies) if self.subsidies else 0
        self.total = self.itemsTotal + self.deliveryTotal
        self.totalWithSubsidy = self.total + self.subsidyTotal


if __name__ == '__main__':
    order = Order({})
    print(Order.__annotations__['id']('123'))
