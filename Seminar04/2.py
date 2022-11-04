def list_positions(collection, prop_check):
    return [i for i, x in enumerate(collection) if prop_check(x)]

def greater_than_zero(item):
    return isinstance(item, int) and item > 0

def is_punctuation(item):
    return item in ",.?!;:<>'\""

def anagram_checker(str1):
    return lambda str2: isinstance(str1, str) and isinstance(str2, str) and sorted(str1) == sorted(str2)

def digits_and_sum_checker(digits, sum):
    def check(nr):
        if not isinstance(nr, int) or nr < 0:
            return False
        if nr == 0:
            return digits == 1 and sum == 0
        total = 0
        count = 0
        while nr:
            total += nr % 10
            count += 1
            nr //= 10
        return count == digits and total == sum
    return check

def main():
    print(list_positions([10, -10, 5, -2, "test", 9.1, -2, 4], greater_than_zero))
    print(list_positions("Cat, Dog. Test: Test;Test2;Test3", is_punctuation))
    print(list_positions(["Abc", "Abb", "Aba", "cbA", "bAc", "aBc", "cAb"], anagram_checker("Abc")))
    print(list_positions([12345, 54321, 9321, 543210, -54321, "54321", 32451], digits_and_sum_checker(5, 15)))

if __name__ == "__main__":
    main()
