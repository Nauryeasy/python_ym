from python_ym import api_objects


class OrdersMixin:
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

        result = self._get_request_post(url=self._api_config.get_order_data_endpoint(), data={}, path_params=path_params)

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

            result = self._get_request_post(url=self._api_config.get_order_data_endpoint(), data={}, query_params=query_params, path_params=path_params)

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

        result = self._get_request_get(url=self._api_config.get_order_solo_endpoint(), query_params=query_params, path_params=path_params)['order']

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

        result = self._get_request_get(url=self._api_config.get_order_endpoint(), query_params=query_params, path_params=path_params)
        result_orders = result['orders']

        orders = []

        for order in result_orders:
            orders.append(api_objects.Order(order))

        for page in range(2, result['pager']['pagesCount'] + 1):
            path_params = {
                'campaignId': campaign_id,
            }

            query_params['page'] = page

            result = self._get_request_get(url=self._api_config.get_order_endpoint(), path_params=path_params, query_params=query_params)

            result_orders = result['orders']
            for order in result_orders:
                orders.append(api_objects.Order(order))

        return orders