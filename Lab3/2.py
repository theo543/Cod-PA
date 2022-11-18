#2a

def sort_lexicografic(nrs):
    return sorted(nrs, key = lambda x : str(x))

print(sort_lexicografic([876, 9, 880, 11188]))

#2b

def sort_lexicografic_reverse(nrs):
    return sorted(nrs, key = lambda x : str(x)[-1::-1])

print(sort_lexicografic_reverse([876, 9, 880, 11188]))

#2c

def sort_length(nrs):
    return sorted(nrs, key = lambda x : len(str(x).strip('-')))

print(sort_length([1111, -22222, 333333]))

#2d

def sort_unique_digits(nrs):
    return sorted(nrs, key = lambda x : len(set(str(x).strip('-'))))

print(sort_unique_digits([111111111, 4113, -987765, 1234]))
