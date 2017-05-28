import json
from json import JSONDecodeError
from urllib.parse import quote, urlsplit, parse_qsl, urlencode, urlunsplit

import re
import requests

BASE_URL = 'https://www.humblebundle.com/store/'


class HumbleDownloader:
    base_url = 'https://www.humblebundle.com/store/api/fetch_chunk?' \
               'path={}&' \
               'component_key=others_grid&' \
               'chunk_index=0'.format  # this is page

    def __init__(self, url):
        self.store_url = self.base_url(self._api_from_url(url))

    def parse_games(self, response):
        try:
            data = json.loads(response.text)
        except JSONDecodeError:
            return []
        data = data['result']['entity_lookup_dict']
        data = [v for k, v in data.items() if '_storefront' in k]
        return data

    def download_games(self):
        games = []
        page = 0
        while True:
            print('parsing page: {}'.format(page))
            url = re.sub('chunk_index=\d+', 'chunk_index={}'.format(page), self.store_url)
            resp = requests.get(url)
            _games = self.parse_games(resp)
            if not _games:
                break
            games.extend(_games)
            page += 1
        return games

    @staticmethod
    def _api_from_url(url):
        url = url.split('?')[0]
        return quote(url.split('/store')[-1], safe='')
