# problema 3: genereaza toate subsirurile crescatoare maximale dintr-un sir dat folosind backtracking

def main():
    arr = [int(x) for x in input("Array = ").split()]
    current = []
    results = [[]]
    def bktrack(pos):
        if pos == len(arr):
            if len(current) > len(results[0]):
                results.clear()
                results.append(current[:])
            elif len(current) == len(results[0]):
                results.append(current[:])
            return
        if not current or arr[pos] >= current[-1]:
            current.append(arr[pos])
            bktrack(pos + 1)
            current.pop()
        bktrack(pos + 1)
    bktrack(0)  
    for r in results:
        print(*r)

if __name__ == '__main__':
    main()
