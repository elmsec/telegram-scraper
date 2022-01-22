from telegram_scraper import TelegramScraper


if __name__ == '__main__':
    ts = TelegramScraper()

    ts.fetch_data(username='botfather')
    if not ts.is_fetched:
        raise IOError("cannot fetch data")

    ts.parse_data()
    if not ts.is_parsed:
        raise ValueError("cannot parse data")

    print('Parsed information: ', ts.information, sep='\n')
