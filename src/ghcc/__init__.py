import requests
from bs4 import BeautifulSoup
from datetime import date


class GHCC:
    url = 'https://github.com/users/{}/contributions'

    def __init__(self, username: str) -> None:
        r = requests.get(self.url.format(username))
        if r.status_code != requests.codes.ok:
            raise ValueError('Incorrect GitHub Username')
        soup = BeautifulSoup(r.content, 'html.parser')
        self.days = []
        table = soup.find('svg').find('g')

        for column in table.find_all('g'):
            for cell in column.find_all('rect'):
                self.days.append(
                    {
                        'count': int(cell['data-count']),
                        'date': cell['data-date'],
                        'level': int(cell['data-level'])
                    }
                )

    @property
    def today(self) -> int:
        if self.days[-1]['date'] != str(date.today()):
            return -1
        return self.days[-1]['count']

    @property
    def streak(self) -> int:
        counter = 0
        for day in reversed(self.days):
            if day['count'] == 0:
                break
            counter += 1
        return counter
