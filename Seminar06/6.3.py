'''
3. Scrieți un algoritm de tip Divide et Impera pentru a rezolva problema turnurilor din 
Hanoi (https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/).
'''
moves = []

def solve(src, dst, spare, len):
    if len == 0:
        return
    solve(src, spare, dst, len - 1)
    moves.append((src, dst))
    solve(spare, dst, src, len - 1)
    pass

def main():
    global moves
    height = int(input("Height: "))
    solve(1, 3, 2, height)
    A = list(reversed(range(1, height + 1)))
    B = []
    C = []
    ref = {1: A, 2: B, 3: C}
    moves = [((a, ref[a]), (b, ref[b])) for a, b in moves]
    for (srcnr, src), (dstnr, dst) in moves:
        print(f"Move from {srcnr}={src} to {dstnr}={dst}")
        if len(src) == 0 or (len(dst) != 0 and src[-1] > dst[-1]):
            print(f"BUG: Invalid move from {src} to {dst}")
            return
        dst.append(src.pop())
    if len(A) != 0 or len(B) != 0 or C != list(reversed(range(1, height + 1))):
        print("BUG: Problem not solved")
        return

if __name__ == '__main__':
    main()
