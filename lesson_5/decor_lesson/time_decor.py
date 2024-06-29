import datetime
from functools import wraps


def check_time(old_function):

    @wraps(old_function)
    def new_function(*args, **kwargs):
        start = datetime.datetime.now()
        result = old_function(*args, **kwargs)
        end = datetime.datetime.now()
        print(
            f"время работы {old_function.__name__} {end - start} с аргументами {args} и {kwargs}"
        )
        return result

    return new_function
