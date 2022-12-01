from functools import cmp_to_key

def comp_implicit(str1, str2):
    if str1 > str2:
        return 1
    elif str1 == str2:
        return 0
    else:
        return -1

def comp_len_lexicografic(str1, str2):
    if len(str1) != len(str2):
        return comp_implicit(len(str1), len(str2))
    return comp_implicit(str1, str2)

def comp_len(str1, str2):
    if len(str1) != len(str2):
        return comp_implicit(len(str1), len(str2))
    return 0

def main():
    with open("cuvinte.txt", "r") as cuvinte, open("cuv_sortate.txt", "w") as cuv_sortate:
        cuv = cuvinte.read().split()
        print(*sorted(cuv, key=cmp_to_key(comp_implicit), reverse=True), file=cuv_sortate)
        print(*sorted(cuv, key=cmp_to_key(comp_len_lexicografic)), file=cuv_sortate)
        print(*sorted(cuv, key=cmp_to_key(comp_len)), file=cuv_sortate)

if __name__ == "__main__":
    main()
