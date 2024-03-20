def custom_sum(x, y):
    """ sum values

    >>> custom_sum(1, 2)
    3

    >>> custom_sum(-2, 3)
    1

    >>> custom_sum('1', 2)
    Traceback (most recent call last):
    ...
    TypeError: can only concatenate str (not "int") to str
    """
    return x + y


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
