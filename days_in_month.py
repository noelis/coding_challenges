def days_in_month(date):
    """How many days are there in a month?

    >>> days_in_month("2 2015")
    28

    >>> days_in_month("1 2017")
    31

    """

    month, year = date.split()

    month = int(month)

    year = int(year)

    calendar = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    leap_year = find_leap_year(year)

    if month == 2 and leap_year:
        return 29

    if not leap_year:
        return calendar[month]
    

def find_leap_year(year):
    """ Determine if year gien is a leap year. 

    >>> find_leap_year(1904)
    True

    >>> find_leap_year(1900)
    False

    >>> find_leap_year(2000)
    True

    """

    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True


if __name__ == '__main__':
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "All test cases passed."
    print
