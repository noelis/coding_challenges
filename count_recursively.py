def count_recursively(lst):
    """ Return number of items in a list, using recursion.

    >>> count_recursively([])
    0

    >>> count_recursively(['a', 'b', 'c'])
    3
    """
    if not lst:
        return 0

    return 1 + count_recursively(lst[1:])



if __name__ == '__main__':
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "All test cases passed."
    print