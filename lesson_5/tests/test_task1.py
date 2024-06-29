import unittest
from unittest_parametrize import parametrize
from unittest_parametrize import ParametrizedTestCase
from check_email_task import check_email
from seasons import check_month
from longest_movie import longest_film

class TestEmail(ParametrizedTestCase):
    @parametrize(
        "email,expected",
        [
            ('vlad@test.ru', True),
            ('vlad@ test.ru', False),
            ('test @org.ru', False),
            ('test . test.ru',False)
        ],
    )
    def test_check_email(self,email: str,expected: bool) -> None:
        result = check_email(email)
        self.assertEqual(expected,result)

class TestSeasons(ParametrizedTestCase):
    @parametrize(
        "season_num,expected",
        [
            (12,'Зима'),
            (6,'Лето'),
            (11,'Осень'),
        ]
    )
    def test_check_season(self, season_num:int,expected:str) -> None:
        result = check_month(season_num)
        self.assertEqual(expected,result)
    
    def test_check_longest_film(self):
        films = ['Аладин', 'Мадагаскар', 'Бетховен']
        expected = 'Мадагаскар'
        result = longest_film(films[0],films[1],films[2])
        self.assertEqual(expected,result)