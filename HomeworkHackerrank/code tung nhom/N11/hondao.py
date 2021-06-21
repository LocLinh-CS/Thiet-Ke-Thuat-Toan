def solved(matrix, stack, r, c):
    count = 0
    for x in range(r):
        for y in range(c):
            if matrix[x][y] == "1":
                stack.append((x, y))
                matrix[x][y] = "X"
                flag = True
                while stack:
                    x, y = stack.pop()
                    for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                        newx = int(x) + dx
                        newy = int(y) + dy
                        if 0 <= newx < r and 0 <= newy < c:
                            if matrix[newx][newy] == "1":
                                stack.append((newx, newy))
                                matrix[newx][newy] = "X"
                        else:
                            flag = False
                if flag:
                    count += 1
    return count


r, c = map(int, input().split())
matrix = []
stack = []
for i in range(r):
    matrix.append([x for x in input().split()])
print(solved(matrix, stack, r, c))