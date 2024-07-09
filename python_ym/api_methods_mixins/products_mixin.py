from python_ym import api_objects


class ProductMixin:

    def get_products(self, business_id: int, offer_ids: list[str] = None) -> list[api_objects.Product]:  # TODO: Сделать фильтры

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

        query_params = {}

        products = []

        while True:

            result = self._get_request_post(url=self._api_config.get_product_endpoint(), data=data,
                                            path_params=path_params, query_params=query_params)

            next_page_token = result['result']['paging'].get('nextPageToken', None)

            result = result['result']['offerMappings']

            for product in result:
                products.append(api_objects.Product({**product['offer'], **product['mapping']}))

            if next_page_token is None:
                break

            query_params = {
                'page_token': next_page_token
            }

        return products

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

        result = self._get_request_post(url=self._api_config.get_productdata_endpoint(), path_params=path_params, data=data)

        result = result['result']['shopSkus']

        products_data = []

        for product_data in result:
            products_data.append(api_objects.ProductData(product_data))

        return products_data