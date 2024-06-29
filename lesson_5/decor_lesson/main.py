import requests

from attempts_decorator import with_attempts
from cached_decor import cached
from print_decor import printable
from time_decor import check_time


@check_time
def swapi_get_people(people_id: int):

    return requests.get(f"https://swapi.py4e.com/api/people/{people_id}").json()


def summator(a, b):
    return a + b


result = swapi_get_people(1)
print(result)
