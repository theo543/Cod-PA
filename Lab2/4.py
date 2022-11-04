str1 = input("str1 = ")
str2 = input("str2 = ")
tracker = [0] * 127

try:

    for char in str1:
        tracker[ord(char)] += 1

    for char in str1:
        tracker[ord(char)] -= 1

except IndexError:
    print("Strings must be ASCII!")
    exit(1)

if tracker.count(0) != 127:
    print("Not anagrams!")
else:
    print("Anagrams!")
