def read(n : int):
    return int(input(f"Day {n} = ").replace(".", ""))

def main():
    n = int(input("n = "))
    result = 0
    prev, today = read(1), read(2)
    max_diff = today - prev
    for i in range(3, n + 1):
        today, prev = read(i), today
        if today - prev > max_diff:
            result = i
            max_diff = today - prev
        pass
    max_diff_s =  ('-' if max_diff < 0 else '') + str(abs(max_diff)).zfill(3)
    print(f"Greatest increase was {max_diff_s[:-2]}.{max_diff_s[-2:]} between day {result + 1} and day {result + 2}.")

if __name__ == "__main__":
    main()
