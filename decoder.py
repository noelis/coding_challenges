def decode(code):
    """ Decode the given string.

    A valid code is a sequence of numbers and letters.

    Each number tells you how many characters to skip before finding a valid letter.

    >>> decode("0h")
    'h'

    >>> decode("0h1ae2bcy")
    'hey'

    >>> decode("2hbc")
    'c'

    """

    decoded_word = ""

    for i in xrange(len(code)):

        if code[i].isdigit():
            num = int(code[i])
            decoded_word += code[i + num + 1]

    return decoded_word


if __name__ == '__main__':
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "All test cases passed."
    print