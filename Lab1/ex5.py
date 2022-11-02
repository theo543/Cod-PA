def read(n : int):
    return int(input(f"x{n} = "))

def main():
    n = int(input("n = "))
    max1, max2 = read(1), read(2)
    if(max1 < max2):
        max1, max2 = max2, max1
    for i in range(3, n + 1):
        x = read(i)
        if x > max1:
            max1, max2 = x, max1
    if max1 == max2:
        print("Imposibil")
    else:
        print(max1, max2)
    pass

if __name__ == "__main__":
    main()
