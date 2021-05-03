from abc import ABC, abstractmethod
import requests


class AbstractParser(ABC):
    @abstractmethod
    def request(self, url):
        pass


class Parser(AbstractParser):
    def request(self, url):
        return requests.get(url)


class ProxyParser(AbstractParser):
    def __init__(self, parser_inst):
        self._parser = parser_inst

    def request(self, url):
        result = self._connect(url)
        if result:
            return result

    def get_text(self, url):
        text_data = self.request(url).text
        return text_data

    def _connect(self, url):
        try:
            result = self._parser.request(url)
        except Exception as exp:
            self._logger(exp)
            return None
        else:
            self._logger('Connection successful')
            self._check_status(result)
            return result

    def _check_status(self, result):
        try:
            result.raise_for_status()
        except Exception as err:
            self._logger(err)
            return False
        else:
            self._logger('Status 200. Success')
            return True

    @staticmethod
    def _logger(msg):
        print(msg)


if __name__ == "__main__":
    parser = Parser()
    parser.request('https://tproger.ru/wp-sdhdsghsdgsdgdsgte.php')
    # Но мы не хендлим ConnectionError и StatusCode

    proxy_parser = ProxyParser(parser)
    proxy_parser.request('https://tproger.ru/wp-sdhdsghsdgsdgdsgte.php')

    print('\n')
    proxy_parser.request('https://tproger.ru/wp-content/plugins/citation-widget/get-quote.php')

    print('\n')
    text = proxy_parser.get_text('https://tproger.ru/wp-content/plugins/citation-widget/get-quote.php')
    print(text)
