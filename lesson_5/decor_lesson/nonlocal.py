from functools import wraps

SOME_LIST = []


def parametrized_decorator(param_1, param_2):
    number_of_calls = 0
    results = []

    def decorator(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            nonlocal number_of_calls
            number_of_calls += 1
            result = old_function(*args, **kwargs)
            results.append(result)
            return result

        return new_function

    return decorator
