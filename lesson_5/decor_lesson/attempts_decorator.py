import time
from functools import wraps


def with_attempts(attempts, timeout):

    def decorator(old_function):

        @wraps(old_function)
        def new_function(*args, **kwargs):
            error = None
            for i in range(1, attempts + 1):
                try:
                    return old_function(*args, **kwargs)
                except Exception as er:
                    error = er
                    print(
                        f"при вызове {old_function.__name__} "
                        f"получена ошибка {er} "
                        f"попытка № {i} из {attempts}"
                    )
                    print("sleep")
                    time.sleep(timeout)
            raise error

        return new_function

    return decorator
