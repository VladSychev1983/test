def summarize(x:int, y:int) -> int:
    if x == -5:
        return 0
    return x + y

def multiply(x: int, y: int) -> int:
    return x * y

def get_info() -> dict:
    return {
        'first_name' : 'Timur',
        'last_name':'Anvartdinov',
        'age': '37',
        'max_age': 40
    }

def test_summarize(a,b, expected):
    result = summarize(a,b)
    try:
        assert expected == result
        print(f'тест провален на параметрах {a}, {b}, {expected}')
    except AssertionError as e:
        print(f'тест провален на параметрах {a}, {b}, {expected}')

if __name__ == '__main__':
    test_summarize(1, 4, 5)
    test_summarize(-6, 4, -2)
    test_summarize(10, -4, 6)
    test_summarize(-5, -4, -9)