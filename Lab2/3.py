import re

text = input("Text = ")
find = input("Find = ")
replace = input("Replace = ")
punctuation = ",.!?<>;:'\""
regex = f"([{punctuation}])"
words = re.split(regex, text)
answer = ''.join([replace if word == find else word for word in words])
print(answer)
