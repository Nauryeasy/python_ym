from .api_object import ApiObject


class Campaign(ApiObject):

    domain: str = None
    id: int = None  # campaign_id
    clientId: int = None

    def __init__(self, data):
        super().__init__(data)


if __name__ == '__main__':
    pass
