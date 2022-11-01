def shift_in_range(nr, shift, start, end):
    if nr < start or nr > end:
        return nr
    return (nr - start + shift) % (end - start + 1) + start;
def shift_char(char, shift):
    if ord(char) in range(ord('a'), ord('z')):
        return chr(shift_in_range(ord(char), shift, ord('a'), ord('z')))
    elif ord(char) in range(ord('A'), ord('Z')):
        return chr(shift_in_range(ord(char), shift, ord('A'), ord('Z')))
    else:
        return char
def main():
    text = input("text=")
    shift = int(input("shift="))
    result = ''.join([shift_char(char, shift) for char in text])
    print(result)


if __name__ == "__main__":
    main()
