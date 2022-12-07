from collections import defaultdict
from typing import DefaultDict

def find_perm(str : str, dict : DefaultDict[str, list]):
    result = [-1] * len(str)
    for i, c in enumerate(str):
        if len(dict[c]) == 0:
            return False
        result[i] = dict[c].pop()
    return result
    pass

def print_perm(perm : list, perm_name : str):
    for i, j in enumerate(perm):
        print(f"{perm_name}({i+1}) = {j+1}")

def main():
    str1 = input("str1=")
    str2 = input("str2=")
    str1pos = defaultdict(list)
    str2pos = defaultdict(list)
    for i, c in enumerate(str1):
        str1pos[c].append(i)
    for i, c in enumerate(str2):
        str2pos[c].append(i)
    perm_p = find_perm(str1, str2pos)
    perm_q = find_perm(str2, str1pos)
    if (perm_p == False) or (perm_q == False):
        print("Not anagrams!")
        return
    print_perm(perm_p, "p")
    print_perm(perm_q, "q")

if __name__ == "__main__":
    main()
