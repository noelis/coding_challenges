def add_to_zero(nums):
    """Given list of ints, return True if any two nums sum to 0.

    >>> add_to_zero([])
    False

    >>> add_to_zero([1])
    False

    >>> add_to_zero([1, 2, 3])
    False

    >>> add_to_zero([1, 2, 3, -2])
    True

    >>> add_to_zero([0, 1, 2, 3])
    True
    """

    if not nums:
        return False
    if len(nums) == 1:
        return False

    set_nums = set(nums)

    for num in nums:
        if -num in set_nums:
            return True

    return False

if __name__ == '__main__':
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "All test cases passed."
    print