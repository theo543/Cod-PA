# problema 1: gaseste toate sub-multiseturile cu suma target folosind backtracking

def main():
    mset = {}
    for x in [int(x) for x in input("Set = ").split()]:
        mset[x] = mset.get(x, 0) + 1
    arr = list(mset.items())
    target = int(input("Target = "))
    results = []
    choices = [0] * len(mset)

    def bktrack(pos, sum):
        if sum > target:
            return
        if pos == len(arr):
            if sum == target:
                results.append(choices[:]) 
            return
        for i in range(arr[pos][1] + 1):
            choices[pos] = i
            bktrack(pos + 1, sum + i * arr[pos][0])

    bktrack(0, 0)
    for r in results:
        output = []
        for nr, choice in zip(arr, r):
            output += [nr[0]] * choice
        print(*output)

if __name__ == '__main__':
    main()
