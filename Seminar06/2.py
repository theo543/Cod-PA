# problema 2: gaseste un sub-multiset cu suma target folosind backtracking

def main():
    mset = {}
    for x in [int(x) for x in input("Set = ").split()]:
        mset[x] = mset.get(x, 0) + 1
    arr = list(mset.items())
    target = int(input("Target = "))
    choices = [0] * len(mset)

    def bktrack(pos, sum):
        if sum > target:
            return
        if pos == len(arr):
            if sum == target:
                return True
            return
        for i in range(arr[pos][1] + 1):
            choices[pos] = i
            if bktrack(pos + 1, sum + i * arr[pos][0]):
                return True

    if bktrack(0, 0):
        output = []
        for nr, choice in zip(arr, choices):
            output += [nr[0]] * choice
        print(*output)
    else:
        print("No solution")

if __name__ == '__main__':
    main()
