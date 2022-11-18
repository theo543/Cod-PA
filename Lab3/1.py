#1a

print(range(1, 10 + 1, 2))

#1b

print([chr(ord('a') + x) for x in range(26)])

#1c

def count_plus_minus(nr):
    return [x * (1 if (x % 2) else -1) for x in range(1, nr + 1)]

print(count_plus_minus(10))

#1d

def odd_numbers(nrs):
    return [x for x in nrs if x % 2]

print(odd_numbers([2,4,5,7,10,11,13,16]))

#1e

def nr_odd_pos(nrs):
    return [nrs[x] for x in range(1, len(nrs), 2)]

print(nr_odd_pos([1,2,3,4,5]))

#1f

def nr_parity_same_as_pos(nrs):
    return [x for i, x in enumerate(nrs) if ((x % 2) == (i % 2))]

print(nr_parity_same_as_pos([2, 4, 1, 7, 5, 1, 8, 10]))

#1g

def adjacent_elems(nrs):
    return [(x, y) for x, y in zip(nrs, nrs[1:])]

print(adjacent_elems([1,2,3,4,5,6,7]))

#1h

def mul_table(n):
    return [[f"{x} * {y} = {x * y}" for y in range(n + 1)] for x in range(n + 1)]

print(*mul_table(10), sep='\n')

#1i

def triangle_counting(n):
    return [[x + 1] * (x + 1) for x in range(n)]

print(*triangle_counting(5), sep='\n')
