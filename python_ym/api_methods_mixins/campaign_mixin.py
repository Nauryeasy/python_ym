from python_ym import api_objects


class CampaignMixin:

    def get_campaigns(self) -> list[api_objects.Campaign]:

        """
        :return: List of Campaign class objects
        """

        result = self._get_request_get(self._api_config.get_campaign_endpoint(), {}, {})['campaigns']

        campaigns = []

        for campaign in result:
            campaigns.append(api_objects.Campaign(campaign))

        return campaigns
