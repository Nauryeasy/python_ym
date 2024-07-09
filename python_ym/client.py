from . import config
from .api_methods_mixins import *


class Client(
    MakeRequestMixin,
    CampaignMixin,
    ProductMixin,
    OrdersMixin,
    PricesMixin,
    WarehousesMixin
):

    def __init__(self, oauth_token, oauth_client_id):
        self._oauth_token = oauth_token
        self._oauth_client_id = oauth_client_id
        self._api_config = config.ApiConfig()


if __name__ == '__main__':
    pass
