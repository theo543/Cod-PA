from math import sqrt

def prime_generator(max_val = -1, max_yields = -1):
    nr = 2
    yields = 0
    while True:
        if nr > max_val and max_val != -1: return
        for p in range(2, int(sqrt(nr)) + 1):
            if (nr % p) == 0:
                break
        else:
            if yields >= max_yields and max_yields != -1: return
            yield nr
            yields += 1
        nr += 1

def main():
    n = int(input("n = "))
    print(*prime_generator(max_val=n))
    print(*prime_generator(max_yields=n))

if __name__ == "__main__":
    main()
