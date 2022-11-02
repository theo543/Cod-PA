def jumps(len : float, percent : int, interval : int, limit : int):
    count = 0
    sum = 0
    while len > 0 and limit > count:
        sum += len
        count += 1
        if (count % interval) == 0:
            len -= len / percent
    return sum

def main():
    x = int(input("x = "))
    n = int(input("n = "))
    p = int(input("p = "))
    m = int(input("m = "))
    print(jumps(x,n,p,m))
    return

if __name__ == "__main__":
    main()
