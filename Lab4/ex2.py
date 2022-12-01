def main():
    punctaje = []
    number = 0
    while True:
        number += 1
        line = input()
        if "-1" in line:
            break
        line = line.split(" ", 1)
        punctaje.append((int(line[0]), line[1], number))
    print(punctaje)
    print({x[0] for x in punctaje})
    dict_punctaje = dict()
    for x in sorted(punctaje, key=lambda p : (-p[0], p[2])):
        dict_punctaje[x[0]] = dict_punctaje.get(x[0], []) + [(x[1], x[2])]
    print(dict_punctaje)

if __name__ == "__main__":
    main()
