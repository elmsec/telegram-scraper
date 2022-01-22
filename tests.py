from unittest import TestCase
from telegram_scraper import TelegramScraper


class TelegramScraperTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.expected = {
            'title': 'BotFather',
            'verified': True,
            'description': (
                'BotFather is the one bot to rule them all. Use it to create '
                'new bot accounts and manage your existing bots.'
            ),
            'image': 'telesco.pe/file/'
        }
        cls.scraper = TelegramScraper()
        cls.username = 'botfather'
        return super().setUpClass()

    def test_fetch_data(self):
        self.scraper.fetch_data(self.username)
        self.assertTrue(self.scraper.is_fetched)
        self.assertGreaterEqual(len(self.scraper.data), 1000)

    def test_parse_data(self):
        self.scraper.parse_data()
        self.assertTrue(self.scraper.is_parsed)
        self.assertEqual(
            self.expected['title'],
            self.scraper.information['title']
        )
        self.assertEqual(
            self.expected['description'],
            self.scraper.information['description']
        )
        self.assertEqual(
            self.expected['verified'],
            self.scraper.information['verified']
        )
        self.assertTrue(
            self.expected['image'] in self.scraper.information['image']
        )
