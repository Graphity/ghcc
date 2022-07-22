import requests
from bs4 import BeautifulSoup


class GHCC:
    url = 'https://github.com/users/{}/contributions'
    
    def __init__(self, username: str) -> None:
        r = requests.get(self.url.format(username))
        if r.status_code != requests.codes.ok:
            raise ValueError('Incorrect GitHub Username')
        soup = BeautifulSoup(r.content, 'html.parser')
        self.calendar = []
        table = soup.find('svg').find('g')

        for column in table.find_all('g'):
            for cell in column.find_all('rect'):
                self.calendar.append(
                    {
                        'count': int(cell['data-count']),
                        'date': cell['data-date'],
                        'level': int(cell['data-level'])
                    }
                )

    @property
    def today(self) -> int:
        return self.calendar[-1]['count']

    @property
    def streak(self) -> int:
        s = 0
        for day in reversed(self.calendar):
            if day['count'] == 0:
                return s
            s += 1
        return s
