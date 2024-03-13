from .api_object import ApiObject

"""
Отчет по товарам
"""

class ProductData(ApiObject):

    class WarehouseOfProductData(ApiObject):
        class Stock(ApiObject):
            type: str = None
            count: int = None

            def __init__(self, data):
                super().__init__(data)

        id: int = None
        name: str = None
        stocks: list[Stock] = None

        def __init__(self, data):
            super().__init__(data)

    shopSku: str = None
    marketSku: int = None
    name: str = None
    price: float = None
    categoryId: int = None
    categoryName: str = None
    warehouses: list[WarehouseOfProductData] = None

    def __init__(self, data):
        super().__init__(data)
