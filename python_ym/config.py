class ApiConfig:
    __BASE_URL = 'https://api.partner.market.yandex.ru/'

    __PRODUCT_ENDPOINT = 'businesses/{businessId}/offer-mappings'
    __CAMPAIGN_ENDPOINT = 'campaigns'
    __ORDER_ENDPOINT = 'campaigns/{campaignId}/orders'
    __ORDER_SOLO_ENDPOINT = 'campaigns/{campaignId}/orders/{orderId}'
    __ORDER_DATA_ENDPOINT = 'campaigns/{campaignId}/stats/orders'
    __WAREHOUSE_ENDPOINT = 'warehouses'
    __PRODUCTDATA_ENDPOINT = 'campaigns/{campaignId}/stats/skus'
    __RECOMMENDATIONS_PRICES_ENDPOINT = '/businesses/{businessId}/offers/recommendations'
    __PRICES_OF_PROMOTION_ENDPOINT = '/campaigns/{campaignId}/offer-prices/suggestions'

    def get_product_endpoint(self):
        return self.__BASE_URL + self.__PRODUCT_ENDPOINT

    def get_campaign_endpoint(self):
        return self.__BASE_URL + self.__CAMPAIGN_ENDPOINT

    def get_order_endpoint(self):
        return self.__BASE_URL + self.__ORDER_ENDPOINT

    def get_order_solo_endpoint(self):
        return self.__BASE_URL + self.__ORDER_SOLO_ENDPOINT

    def get_order_data_endpoint(self):
        return self.__BASE_URL + self.__ORDER_DATA_ENDPOINT

    def get_warehouse_endpoint(self):
        return self.__BASE_URL + self.__WAREHOUSE_ENDPOINT

    def get_productdata_endpoint(self):
        return self.__BASE_URL + self.__PRODUCTDATA_ENDPOINT

    def get_recommendations_prices_endpoint(self):
        return self.__BASE_URL + self.__RECOMMENDATIONS_PRICES_ENDPOINT

    def get_prices_of_promotion_endpoint(self):
        return self.__BASE_URL + self.__PRICES_OF_PROMOTION_ENDPOINT
