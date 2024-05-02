from .api_object import ApiObject


class Campaign(ApiObject):

    class Business(ApiObject):
        id: int = None
        name: str = None

        def __init__(self, data):
            super().__init__(data)

    """URL магазина."""
    domain: str = None
    """Идентификатор кампании."""
    id: int = None  # campaign_id
    """Идентификатор плательщика в Яндекс Балансе."""
    clientId: int = None
    """Информация о кабинете."""
    business: Business = None

    def __init__(self, data):
        super().__init__(data)


if __name__ == '__main__':
    pass
