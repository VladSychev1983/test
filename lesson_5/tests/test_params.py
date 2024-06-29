import unittest
from simple_test import summarize,get_info

server = "PROD"

class TestMain(unittest.TestCase):
    #при необходимости можно пропускать тесты на нереализованный функционал.
    #@unittest.skipIf(server == "PROD", "Не реализована")
    #если знаем что тест ожидаемо падает.
    #@unittest.expectedFailure
    # если надо пропустить тест
    @unittest.skip 
    def test_summarize_with_params(self):
        for i, (a, b, expected) in enumerate([
            (5, 7, 12),
            (-5, 7, 2),
            (5, -7, -2),
            ]):
            with self.subTest(i):
                result = summarize(a,b)
                self.assertEqual(expected,result)
    
    def test_get_info(self):
        expected = {
        'first_name' : 'Timur',
        'last_name':'Anvartdinov',
        'age': '37',
        'max_age': 40
    }
        result = get_info()
        self.assertDictEqual(expected,result)
    
    def test_regexp(self):
        date = '2024-06-18'
        pattern = r'\d{4}-\d{2}-\d{2}'
        self.assertRegex(date,pattern)

        