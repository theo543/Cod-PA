n = int(input("n = "))
if n & (n - 1) == 0:
    print(n)
else:
    while n & (n - 1):
        n = n & (n - 1)
    print(n << 1)
