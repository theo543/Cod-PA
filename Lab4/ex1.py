def main():
    with open("test.in", "r") as input, open("test.out", "w") as output:
        nota = 1
        for line in input.read().split():
            nr1, nr2, result = [int(x) for x in line.replace("=", "*").split("*")]
            if nr1 * nr2 != result:
                line = line + f" Gresit {nr1 * nr2}"
            else:
                nota += 1
                line = line + " Corect"
            print(line, file=output)
        print(f"Nota {nota}", file=output)

if __name__ == "__main__":
    main()
