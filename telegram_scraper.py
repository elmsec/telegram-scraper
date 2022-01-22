import requests
from bs4 import BeautifulSoup


class TelegramScraper:
    """
    Scrapes Telegram content information from the official Telegram
    website https://t.me
    """

    _URL_TEMPLATE = "https://t.me/%(username)s"
    _DATA = None
    _INFORMATION = {}
    _DATA_MAP = {
        'title': 'div.tgme_page_title > span[dir=auto]',
        'verified': 'div.tgme_page_title > i.verified-icon',
        'description': 'div.tgme_page_description',
        'image': 'img.tgme_page_photo_image[src]',
    }

    def __init__(self):
        pass

    def fetch_data(self, username: str) -> bool:
        result = requests.get(self._URL_TEMPLATE % dict(username=username))
        if result.status_code >= 200 and result.status_code < 300:
            self._DATA = result.text
            return True
        return False

    def parse_data(self) -> dict:
        bs = BeautifulSoup(self.data, 'html.parser')

        title = bs.select_one(self._DATA_MAP['title'])
        verified = bs.select_one(self._DATA_MAP['verified']) is not None
        description = bs.select_one(self._DATA_MAP['description'])
        image = bs.select_one(self._DATA_MAP['image'])

        self._INFORMATION = {
            'title': title.string if title else "",
            'verified': verified,
            'description': description.text if description else "",
            'image': image['src'] if image else ""
        }

    @property
    def data(self) -> str:
        return self._DATA

    @property
    def information(self) -> dict:
        return self._INFORMATION

    @property
    def is_fetched(self) -> bool:
        return self._DATA is not None

    @property
    def is_parsed(self) -> bool:
        return len(self._INFORMATION.items()) > 0
