from random import choice


def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive)."""

    nums = range(1,11)
    lucky_nums = []

    for i in xrange(n):
        random_num = choice(nums)
        lucky_nums.append(random_num)
        nums.remove(random_num)

    return lucky_nums

print lucky_numbers(2)
print lucky_numbers(10)
print lucky_numbers(0)