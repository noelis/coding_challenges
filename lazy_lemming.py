def find_longest_path(num_holes, cafes):

    # Tracks the distance of the lemming that is the furthest from its nearest cafe (so far)
    furthest_lemming = 0

    for i in xrange(num_holes):

        # Iterate through cafe list 
        # to create a new list of the distances between the lemming and all cafes
        # then finds the smallest number in the list and sets the dist variable

        dist = min([abs(i - cafe) for cafe in cafes])

        # compares the furthest lemming and distance so far, finds max
        furthest_lemming = max(furthest_lemming, dist)

    return furthest_lemming

print find_longest_path(6, [2, 4])