import time


def time_spent(fn):
    """ it'll return a modified function with a time tracker """

    def modified_fn(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        seconds = end_time - start_time
        print(f'{fn.__name__} took {seconds:.2f} seconds')
        return result

    return modified_fn


def dummy_fn(seconds: int) -> str:
    """ dummy example to show how it works """
    time.sleep(seconds)
    return 'Hello World!'


def main():
    dummy_fn_tracked = time_spent(dummy_fn)

    r = dummy_fn_tracked(5)
    print(r)


if __name__ == '__main__':
    main()
