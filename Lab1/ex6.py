def build_output(s : str, rng):
    nr = 0
    for i in rng:
        for _ in range(0, s.count(chr(ord('0') + i))):
            nr *= 10
            nr += i
    return nr

def main():
    n = str(int(input("n = ")))
    print(build_output(n, range(0, 10)))
    print(build_output(n, range(9, -1, -1)))
    pass

if __name__ == "__main__":
    main()
