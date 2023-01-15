import time

from tracker import timer


def dummy_fn(seconds: int) -> str:
    """ dummy example to show how it works """
    time.sleep(seconds)
    return 'Hello World!'


def main():
    dummy_fn_tracked = timer(dummy_fn)

    r = dummy_fn_tracked(5)
    print(r)


if __name__ == '__main__':
    main()
