def main():
    count = [0] * 26
    str1 = input("str1=")
    str2 = input("str2=")
    for c in (ord(c) - ord('a') for c in str1):
        count[c] += 1
    for c in (ord(c) - ord('a') for c in str2):
        count[c] -= 1
    for v in count:
        if v != 0:
            print("Not anagrams!")
            break
    else:
        print("Anagrams.")
    return

if __name__ == "__main__":
    main()
