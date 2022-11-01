def main():
    text = input().lower()
    punctuation = ',.?!;:\'\"'
    text = set(text.translate({ord(c) : ord(' ') for c in punctuation}).split(' '))
    text.remove('')
    print(text)
    print(f"There are {len(text)} unique words.")

if __name__ == "__main__":
    main()
