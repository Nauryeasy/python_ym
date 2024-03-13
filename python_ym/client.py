import requests

import api_objects
import config


class Client:

    def __init__(self, oauth_token, oauth_client_id):
        self.__oauth_token = oauth_token
        self.__oauth_client_id = oauth_client_id
        self.__api_config = config.ApiConfig()

    def get_product_data(self, campaign_id: int, shop_skus: list[str]) -> list[api_objects.ProductData]:
        """
        :param shop_skus: List of skus
        :param campaign_id: Shop id. Can be obtained in your personal account or using the get_campaigns method
        :return: List of ProductData class objects
        """

        path_params = {
            'campaignId': campaign_id
        }

        data = {
            'shopSkus': shop_skus
        }

        result = self.__get_request_post(url=self.__api_config.get_productdata_endpoint(), path_params=path_params, data=data)

        result = result['result']['shopSkus']

        products_data = []

        for product_data in result:
            products_data.append(api_objects.ProductData(product_data))

        return products_data

    def get_warehouses(self) -> list[api_objects.Warehouse]:

        result = self.__get_request_get(url=self.__api_config.get_warehouse_endpoint(), path_params={})['result']['warehouses']

        warehouses = []

        for warehouse in result:
            warehouses.append(api_objects.Warehouse(warehouse))

        return warehouses

    def get_orders_data(self, business_id: int, campaign_id: int, all: bool = False,  orders_ids: list[int] = None) -> list[
        api_objects.OrderData]:
        """
        :param campaign_id: Shop id. Can be obtained in your personal account or using the get_campaigns method
        :param orders_ids: List of order IDs
        :return: List of OrderData class objects
        """

        path_params = {
            'campaignId': campaign_id,
            'businessId': business_id
        }

        # data = {
        #     'orders': orders_ids
        # }

        result = self.__get_request_post(url=self.__api_config.get_order_data_endpoint(), data={}, path_params=path_params)

        nextPageToken = result['result']['paging']['nextPageToken']
        orders_result = result['result']['orders']

        orders = []

        while nextPageToken is not None:
            for order in orders_result:
                orders.append(api_objects.OrderData(order))

            if not all:
                break

            query_params = {
                'page_token': nextPageToken
            }

            result = self.__get_request_post(url=self.__api_config.get_order_data_endpoint(), data={}, query_params=query_params, path_params=path_params)

            try:
                nextPageToken = result['result']['paging']['nextPageToken']
            except:
                nextPageToken = None
            orders_result = result['result']['orders']

        return orders

    def get_order(self, business_id: int, campaign_id: int, order_id: int) -> api_objects.Order:
        """
        :param campaign_id: Shop id. Can be obtained in your personal account or using the get_campaigns method
        :param order_id: Id of order
        :return: Object of Order class
        """

        path_params = {
            'campaignId': campaign_id,
            'businessId': business_id
        }

        query_params = {
            'orderId': order_id,
        }

        result = self.__get_request_get(url=self.__api_config.get_order_solo_endpoint(), query_params=query_params, path_params=path_params)['order']

        order = api_objects.Order(result)

        return order

    def get_orders(self, campaign_id: int, from_date: str = None, to_date: str = None) -> list[api_objects.Order]:  # Сделать фильтры

        """
        :param campaign_id: Shop id. Can be obtained in your personal account or using the get_campaigns method
        :param all:
        :param from_date: from date for filter '01-01-2022'
        :param to_date: to date for filter '01-02-2022'
        :return: List of Order class objects
        """

        path_params = {
            'campaignId': campaign_id,
        }

        query_params = {
            'fromDate': from_date,
            'toDate': to_date,
            'pageSize': 50
        }

        result = self.__get_request_get(url=self.__api_config.get_order_endpoint(), query_params=query_params, path_params=path_params)
        result_orders = result['orders']

        orders = []

        for order in result_orders:
            orders.append(api_objects.Order(order))

        for page in range(2, result['pager']['pagesCount'] + 1):
            path_params = {
                'campaignId': campaign_id,
            }

            query_params['page'] = page

            result = self.__get_request_get(url=self.__api_config.get_order_endpoint(), path_params=path_params, query_params=query_params)

            result_orders = result['orders']
            for order in result_orders:
                orders.append(api_objects.Order(order))

        return orders

    def get_products(self, business_id: int, offer_ids: list[str] = None) -> list[api_objects.Product]:  # Сделать фильтры

        """
        :param offer_ids: List of Shop SKU
        :return: List of Product class objects
        """

        path_params = {
            'businessId': business_id
        }

        data = {
            'offerIds': offer_ids
        }
        result = self.__get_request_post(url=self.__api_config.get_product_endpoint(), data=data, path_params=path_params)['result']['offerMappings']

        products = []

        for product in result:
            products.append(api_objects.Product({**product['offer'], **product['mapping']}))

        return products

    def get_campaigns(self) -> list[api_objects.Campaign]:

        """
        :return: List of Campaign class objects
        """

        result = self.__get_request_get(self.__api_config.get_campaign_endpoint(), {}, {})['campaigns']

        campaigns = []

        for campaign in result:
            campaigns.append(api_objects.Campaign(campaign))

        return campaigns

    def __get_headers_get(self):
        return {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20100101 Firefox/12.0',
            'Accept': 'application/json',
            'Accept-Language': 'en-en,ru;q=0.8,en-us;q=0.5,en;q=0.3',

            'Connection': 'keep-close',

            'Authorization': f'OAuth oauth_token="{self.__oauth_token}", oauth_client_id="{self.__oauth_client_id}"'
        }

    def __get_headers_post(self):
        return {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20100101 Firefox/12.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-en,ru;q=0.8,en-us;q=0.5,en;q=0.3',

            'Connection': 'keep-close',

            'Authorization': f'OAuth oauth_token="{self.__oauth_token}", oauth_client_id="{self.__oauth_client_id}"'
        }

    def __get_request_get(self, url: str, path_params: dict, query_params: dict = None) -> dict:
        url = url.format(**path_params)
        headers = self.__get_headers_get()

        response = requests.get(url, headers=headers, params=query_params)

        return response.json()

    def __get_request_post(self, url: str, data: dict, path_params: dict, query_params: dict = None) -> dict:
        url = url.format(**path_params)
        headers = self.__get_headers_post()

        response = requests.post(url, headers=headers, json=data, params=query_params)

        return response.json()


if __name__ == '__main__':
    pass
