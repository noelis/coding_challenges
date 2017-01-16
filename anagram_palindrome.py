from collections import Counter

def is_anagram_of_palindrome(word):
    """ Is the word an anagram of a palindrome?

    anagram: a word formed by rearranging the letters of another.
    ie: Cinema > iceman

    palindrome: a word that reads the same backwards/forwards.
    ie: madam, racecar

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

    >>> is_anagram_of_palindrome("aaa")
    True
    """

    word_cnt = Counter(word)
    single_letter = 0

    for count in word_cnt.values():
        if count == 1:
            single_letter += 1

    if single_letter > 1:
        return False
    else:
        return True


if __name__ == '__main__':
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "All test cases passed."
    print
