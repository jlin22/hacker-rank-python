def minimum_bribes(q):
    '''Input:
    q is an array of people, a permutation of 1-len(q)
    People can bribe each other, swapping positions
    People can only be bribed twice, so swapped twice
    If a state is too chaotic, return 'Too chaotic'
    '''

    inversions = 0
    for i in range(len(q)):
        if q[i] > i + 3 or q[i] < i - 1:
            return 'Too chaotic'
        inversions += abs(i + 1 - q[i])
    return inversions // 2

print(minimum_bribes([2, 1, 5, 3, 4]))
print(minimum_bribes([2, 5, 1, 3, 2]))
