from datetime import datetime


def timeit(func):
    def wrap(*args, **kwargs):
        start = datetime.now()
        res = func(*args, **kwargs)
        elapsed = (datetime.now() - start)
        print(f'elapsed {elapsed}')
        return res
    return wrap
