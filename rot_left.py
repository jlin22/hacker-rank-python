def rot_left(a, d):
    ''' Inputs:
    a: an array of integers
    d: the number of rotations
    Output:
    an array left rotated d times
    '''

    # calculate the number of times we need to left shift
    shifts = d % len(a)

    # Create a queue of a[:shift-1]
    queue = []
    for i in range(shifts):
        queue.append(a[i])

    # Create the output array
    out = []

    # Add the elements a[shift:] to out
    for element in a[shifts:]:
        out.append(element)
    
    # Add the elements in the queue to the output array
    for element in queue:
        out.append(element)
    
    return out
    
# Test cases
print(rot_left(list(range(1, 10)), 5))
print(list(range(1,6)))
print(rot_left(list(range(1,6)),2))

