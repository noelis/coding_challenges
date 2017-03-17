def find_longest_path(num_holes, cafes):

    furthest_lemming = None

    for i in xrange(num_holes):

        for cafe in cafes:

            mid_point = num_holes / 2

            if i < mid_point and cafe < mid_point and furthest_lemming < cafe - i:
                furthest_lemming = cafe - i
                break
            if i >= mid_point and cafe >= mid_point and furthest_lemming < abs(i - cafe):
                furthest_lemming = abs(i - cafe)
                break
            break    

    return furthest_lemming

print find_longest_path(6, [2, 4])

