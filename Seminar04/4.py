def find_strings(n : int, *strings : str):
    ret_list = []
    for str in strings:
        if len(str) == n:
            print("Found string.")
            ret_list.append(str)
    print("Exiting.")
    return ret_list

def find_strings_generator(n : int, *strings : str):
    for str in strings:
        if len(str) == n:
            print("Found string.")
            yield str
    print("Exiting.")

def main():
    print("With function:\n")
    for str in find_strings(4, "Test1", "Test12", "Test", "Abcd", "Tes1"):
        print(str)
    print("\nWith generator:\n")
    for str in find_strings_generator(4, "Test1", "Test12", "Test", "Abcd", "Tes1"):
        print(str)

if __name__ == "__main__":
    main()
