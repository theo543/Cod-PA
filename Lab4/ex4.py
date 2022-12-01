def min_max(*args):
    try:
        nrs = [int(i) for i in args]
        return min(nrs), max(nrs)
    except (TypeError, ValueError) as e:
        return None

def main():
    try:
        with open("numere.txt", "r") as numere:
            ret = min_max(*numere.read().split())
            print(ret)
            if ret != None:
                with open("impartire.txt", "w") as impartire:
                    impartit = float(ret[1]) / float(ret[0])
                    print(impartit, file=impartire)

    except (FileNotFoundError, OSError, ValueError, ZeroDivisionError) as e:
        print(e)

if __name__ == "__main__":
    main()
