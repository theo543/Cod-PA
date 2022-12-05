import random

def generate(n : int, m : int):
    nrs = sorted([random.randint(1, 1000) for _ in range(n * m)])
    mat = [[-1 for _ in range(n)] for _ in range(m)]
    for diag in range(m + n - 1):
        i, j = None, None
        if diag >= n:
            i = 0
            j = m - 1 - (diag - n + 1)
        else:
            i = n - diag - 1
            j = m - 1
        while i in range(0, n) and j in range(0, m):
            mat[j][i] = nrs.pop()
            i += 1
            j -= 1
    return mat

def output(mat : list[list[int]]):
    nrlen = len(str(mat[-1][-1]))
    for line in mat:
        print(*[str(x).rjust(nrlen) for x in line])

def verify(mat : list[list[int]]):
    for i in range(0, len(mat)):
        for j in range(0, len(mat[i])):
            try:
                if mat[i + 1][j] < mat[i][j] or mat[i][j + 1] < mat[i][j]:
                    return False
            except IndexError:
                pass
    return True

def mn_search(mat : list[list[int]], x : int):
    for i in range(0, len(mat)):
        for j in range(0, len(mat[i])):
            if mat[i][j] == x:
                return i, j
    return None

def binary_search(line : list[int], x : int):
    l, r = 0, len(line) - 1
    while l != r:
        m = (l + r + 1) // 2
        if line[m] > x:
            r = m - 1
        else:
            l = m
    return line[l], l

def m_log_n_search(mat : list[list[int]], x : int):
    for i in range(0, len(mat)):
        val, j = binary_search(mat[i], x)
        if val == x:
            return i, j
    return None

def m_plus_n_search(mat : list[list[int]], x : int):
    i = 0
    j = len(mat[0]) - 1
    while j in range(0, len(mat[0])) and i in range(0, len(mat)):
        if mat[i][j] > x:
            j -= 1
        elif mat[i][j] < x:
            i += 1
        else:
            return i, j
    return None

def main():
    m = int(input("m = "))
    n = int(input("n = "))
    mat = generate(n, m)
    assert(verify(mat))
    output(mat)
    x = int(input("x = "))
    print(mn_search(mat, x))
    print(m_log_n_search(mat, x))
    print(m_plus_n_search(mat, x))

if __name__ == "__main__":
    main()
