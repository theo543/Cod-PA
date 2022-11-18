#5a

n = int(input("n = "))
mat = [[1 + i + y * n for i in range(n)] for y in range(n)]
for line in mat:
    print(*[str(x).rjust(len(str(n*n))) for x in line])

positions : list[tuple[int, int]] = [(0, 0)] * (n * n)
positions[0] = (0, 0)
posi = 1
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
mode = 0
dir = dirs[mode]
vis = [[False] * n for _ in range(n)]
vis[0][0] = True

while posi < len(positions):
    p = (positions[posi - 1][0] + dir[0], positions[posi - 1][1] + dir[1])
    if p[0] not in range(0, n) or p[1] not in range(0, n) or vis[p[0]][p[1]]:
        mode = (mode + 1) % 4
        dir = dirs[mode]
    else:
        vis[p[0]][p[1]] = True
        positions[posi] = p
        posi += 1

print([mat[x][y] for x, y in positions])
