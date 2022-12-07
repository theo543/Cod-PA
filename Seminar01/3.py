x = int(input("x = "))
y = int(input("y = "))
xor = x ^ y
bits = 0
while xor:
    bits += 1
    xor &= (xor - 1)
print(bits)
