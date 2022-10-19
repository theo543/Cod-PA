n = int(input("n = "))
bits = 0
while n:
    bits += not (n & 1)
    n >>= 1
print(bits)
