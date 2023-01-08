# problema 4: gaseste lungimea maxima a unui subsir crescator folosind programare dinamica

def main():
    arr = [int(x) for x in input("Array = ").split()]
    dp = [min(arr) - 1]
    for i in range(len(arr)):
        for j in reversed(range(len(dp))):
            if arr[i] >= dp[j]:
                if len(dp) > (j + 1):
                    dp[j + 1] = min(arr[i], dp[j + 1])
                else:
                    dp.append(arr[i])
    maxlen = len(dp) - 1
    for i in range(len(arr)):
        subarr = arr[i:i + maxlen]
        for j in range(1, len(subarr)):
            if subarr[j] < subarr[j - 1]:
                subarr = None
                break
    print(len(dp) - 1)
if __name__ == '__main__':
    main()
