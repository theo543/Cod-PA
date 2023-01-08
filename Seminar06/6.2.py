'''
2.  Se  consideră  o  listă  sortată  crescător  de  numere  întregi.  Scrieți  o  funcție  cu 
complexitate minimă care să furnizeze numărul de apariții ale unei valori în listă. De 
exemplu, în lista [1, 1, 2, 2, 2, 2, 4, 4, 4, 4, 5] valoarea 2 apare de 4 ori.
'''
def bs_left(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] == target:
            right = mid
        else:
            right = mid - 1
    if arr[left] == target:
        return left
    return -1
def bs_right(arr, target):
    left = 0
    right = len(arr) - 1
    while left != right:
        mid = (left + right + 1) // 2 # roundup
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] == target:
            left = mid
        else:
            left = mid + 1
    if arr[left] == target:
        return left
    return -1
def solve(arr, target):
    left = bs_left(arr, target)
    right = bs_right(arr, target)
    if left == -1 or right == -1:
        return 0
    return right - left + 1

def main():
    test = [1, 1, 2, 2, 2, 2, 4, 4, 4, 4, 5]
    for i in range(1, 5 + 1):
        print(f"{i}->{solve(test, i)} times")

if __name__ == '__main__':
    main()
