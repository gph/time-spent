import time


def timer(fn):
    """ it'll return a modified function with a time tracker """

    def modified_fn(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        seconds = end_time - start_time
        print(f'TIME_SPENT: {fn.__name__} took {seconds:.2f} seconds')
        return result

    return modified_fn
