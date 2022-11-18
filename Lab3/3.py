from string import punctuation
with open('propo.txt') as f:
    data = f.readline()
    sentence = data.translate({ord(x) : ord(' ') for x in punctuation})
    counter = dict()
    for word in sentence.split():
        counter[word] = counter.get(word, 0) + 1
    rev_counter = sorted([(b, a) for a, b in counter.items()])
    print(rev_counter)
    min_word = rev_counter[0][1]
    max_word = ''
    for x in range(len(rev_counter) - 1, -1, -1):
        if rev_counter[x][0] != rev_counter[-1][0]:
            break
        max_word = rev_counter[x][1]
    print(f"Least common word = {min_word}\nMost common word  = {max_word}")
