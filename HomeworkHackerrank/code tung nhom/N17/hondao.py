def numIslands(mx, n, m):
    if not mx:
        return 0

    def isIsland(i, j):
        mx[i][j] = 0

        for (x, y) in [(i, j-1), (i-1, j), (i, j+1), (i+1, j)]:
            if 0 <= x < n and 0 <= y < m and mx[x][y] == 1:
                isIsland(x, y)

    res = 0
    for i in range(1,n):
        for j in range(1,m):
            if mx[i][j] == 1:
                isIsland(i, j)
                res += 1
                
    return res


mx = []
n, m = map(int, input().split())
for i in range(n):
    s = list(map(int, input().split()))
    mx.append(s)

print(numIslands(mx, n, m))
