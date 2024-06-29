from functools import wraps


def decorator(old_function):

    @wraps(old_function)
    def new_function(*args, **kwargs):
        # код до вызова исходной функции
        result = old_function(*args, **kwargs)
        # код после вызова исходной функции
        return result

    return new_function


@decorator
def foo():
    pass


foo = decorator(foo)

print(foo.__name__)


def parametrized_decorator(param_1, param_2):

    def decorator(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            # param1
            # param2
            # код до вызова исходной функции
            result = old_function(*args, **kwargs)
            # код после вызова исходной функции
            return result

        return new_function

    return decorator
