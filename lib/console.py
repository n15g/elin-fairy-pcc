from functools import wraps


class COLOR:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[39m'


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{COLOR.BLUE}---[{COLOR.CYAN}{func.__qualname__}{COLOR.BLUE}]---{COLOR.RESET}")
        return func(*args, **kwargs)

    return wrapper
