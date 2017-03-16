def count_recursively(lst):
    """ Count the number of items in a list using recursion.
    
    >>> count_recursively([])
    0

    >>> count_recursively(["a", "b", "c", "d"])
    4

    >>> count_recursively([[], [], [], [], [], []])
    6

    """

    if lst == []:
        return 0

    return 1 + count_recursively(lst[1:])

if __name__ == '__main__':
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "All test cases passed."
    print