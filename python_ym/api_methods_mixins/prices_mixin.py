from typing import Tuple

from python_ym import api_objects


class PricesMixin:
    def get_prices_of_promotion(self, campaign_id: int, offers: list[dict]) -> list[api_objects.PricesOfPromotion]:
        """
        :param campaign_id: Shop id. Can be obtained in your personal account or using the get_campaigns method
        :param offers: List of dictionaries, where each contains the key offerId (str) and marketSku (int)
        :return: List of PricesOfPromotion class objects
        """

        path_params = {
            'campaignId': campaign_id
        }

        data = {
            'offers': offers
        }

        result = self._get_request_post(
            url=self._api_config.get_prices_of_promotion_endpoint(),
            data=data,
            path_params=path_params
        )['result']['offers']

        prices_of_promotion = []

        for offer in result:
            prices_of_promotion.append(api_objects.PricesOfPromotion(offer))

        return prices_of_promotion

    def get_recommendations_prices(self, business_id: int) -> Tuple[list[api_objects.StatePrices],
                                                                    list[api_objects.RecommendationPrices]]:
        """TODO: Написать получение результатов из нескольких страниц"""
        """
        :param business_id: Business id. Can be obtained in your personal account or using the get_campaigns method
        :return: List of StatePrices class objects and List of RecommendationPrices class objects
        """

        path_params = {
            'businessId': business_id
        }

        result = self._get_request_post(url=self._api_config.get_recommendations_prices_endpoint(),
                                         path_params=path_params,
                                         data={}
                                         )['result']['offerRecommendations']

        states_prices = []
        recommendations_prices = []

        for recommendation in result:
            recommendation['recommendation']['offerId'] = recommendation['offer']['offerId']
            states_prices.append(api_objects.StatePrices(recommendation['offer']))
            recommendations_prices.append(api_objects.RecommendationPrices(recommendation['recommendation']))

        return states_prices, recommendations_prices