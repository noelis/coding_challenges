def find_magic_number(num):
    """ Using binary search, create a function that finds the user's number that is between 1 -100. 

    Once the function finds the number, return the number of guesses it took to find it.

    >>> find_magic_number(31)
    4

    >>> find_magic_number(79)
    6

    >>> find_magic_number(1)
    6

    >>> find_magic_number(100)
    7

    >>> find_magic_number(19)
    6

    >>> find_magic_number(50)
    1
    """

    assert 0 < num < 101, "The number must be between 1-100, please pick a different number."

    num_guesses = 0
    high_num = 101
    low_num = 0
    guess = None

    while guess != num:
        # Our guess will always be in halfway point of our previous high/low numbers
        # We take the current high - low numbers, divide by 2 so we get the halfwat
        # point, then we add the lowest number since that will be our new starting point.

        # In each gues we're shortening the range of numbers we have to guess by 50%.
        guess = (high_num - low_num) / 2 + low_num

        if num > guess:
            low_num = guess
        if num < guess:
            high_num = guess

        num_guesses += 1

    return num_guesses

print find_magic_number(50)

if __name__ == '__main__':
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "All test cases passed."
    print