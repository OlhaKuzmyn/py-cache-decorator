from typing import Callable


def cache(func: Callable) -> Callable:
    stored_res = {}

    def wrapper(*args, **kwargs) -> Callable:
        if args in stored_res:
            print("Getting from cache")
            return stored_res[args]
        print("Calculating new result")
        result = func(*args, **kwargs)
        stored_res[args] = result
        return result
    return wrapper
