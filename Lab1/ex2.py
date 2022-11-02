def gcd(a : int, b : int):
    while a % b:
        a, b = b, a % b
    return b

def main():
    a = int(input("L1 = "))
    b = int(input("L2 = "))
    print(gcd(a, b))
    pass

if __name__ == "__main__":
    main()
