import pytest

from PhoneBook import PhoneBook
from simple_test import summarize,get_info

@pytest.mark.parametrize(
        'a,b,expected',
        (
            [5, 7, 12],
            [-5, 7, 2],
            [5, -7, -2],

        )
)
# пропустить тест.
#@pytest.mark.skip(reason='не хочу')
#@pytest.mark.skipif(True,reason='не хочу')
#если знаем что падает.
#@pytest.mark.xfail
def test_summaraze(a,b,expected):
    result = summarize(a,b)
    assert result == expected