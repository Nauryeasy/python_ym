from .api_object import ApiObject


class Warehouse(ApiObject):

    id: int = None
    name: str = None

    def __init__(self, data):
        super().__init__(data)


if __name__ == '__main__':
    pass
