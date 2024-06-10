import requests


class SwapiPeople:

    def __init__(self):
        pass

    def __iter__(self):
        self.next_link = "https://swapi.py4e.com/api/people/"
        self.results = iter([])
        return self

    def _get_results(self):
        response = requests.get(self.next_link).json()
        self.next_link = response["next"]
        self.results = iter(response["results"])

    def _get_item(self):
        try:
            item = next(self.results)
        except StopIteration:
            item = None
        return item

    def __next__(self):
        item = self._get_item()
        if item is None:
            if self.next_link is None:
                raise StopIteration
            self._get_results()
            item = self._get_item()
        return item


people = list(SwapiPeople())
