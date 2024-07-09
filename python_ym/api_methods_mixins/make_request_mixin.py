import requests


class MakeRequestMixin:

    def __get_headers_get(self):
        return {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20100101 Firefox/12.0',
            'Accept': 'application/json',
            'Accept-Language': 'en-en,ru;q=0.8,en-us;q=0.5,en;q=0.3',

            'Connection': 'keep-close',

            'Authorization': f'OAuth oauth_token="{self._oauth_token}", oauth_client_id="{self._oauth_client_id}"'
        }

    def __get_headers_post(self):
        return {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20100101 Firefox/12.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-en,ru;q=0.8,en-us;q=0.5,en;q=0.3',

            'Connection': 'keep-close',

            'Authorization': f'OAuth oauth_token="{self._oauth_token}", oauth_client_id="{self._oauth_client_id}"'
        }

    def _get_request_get(self, url: str, path_params: dict, query_params: dict = None) -> dict:
        url = url.format(**path_params)
        headers = self.__get_headers_get()

        response = requests.get(url, headers=headers, params=query_params)

        return response.json()

    def _get_request_post(self, url: str, data: dict, path_params: dict, query_params: dict = None) -> dict:
        url = url.format(**path_params)
        headers = self.__get_headers_post()

        response = requests.post(url, headers=headers, json=data, params=query_params)

        return response.json()