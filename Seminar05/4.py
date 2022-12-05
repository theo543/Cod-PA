def main():
    n = int(input("n = "))
    A = [float(input(f"A[{i}] = ")) for i in range(n + 1)]
    x = float(input("x = "))
    x_vals = [(x ** i, i) for i in range(n + 1)]
    x_vals.sort()
    A.sort()
    eq = sorted(zip(x_vals, A), key = lambda item : item[0][1])
    print("P(x) = ", end="")
    print(*reversed([f"{cf}x^{i}" for [x_val, i], cf in eq]), sep=" + ")
    print(f"P({x}) = {sum([x_val * cf for [x_val, i], cf in eq])}")

if __name__ == "__main__":
    main()
