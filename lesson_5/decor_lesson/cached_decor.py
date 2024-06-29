from functools import wraps


def cached(old_function):

    cache = {}

    @wraps(old_function)
    def new_function(*args, **kwargs):
        key = f"{args}_{kwargs}"
        if key in cache:
            return cache[key]
        result = old_function(*args, **kwargs)
        cache[key] = result
        return result

    new_function.__name__ = old_function.__name__
    return new_function
