m = int(input())
arr = [int(x) for x in input().split()]
s = sum(arr)
arr.sort()


def solved(arr, m, s):
    if s % 2 != 0:
        return False
    halfSumArr = s // 2
    matrix = [[False] * (halfSumArr + 1) for x in range(m)]
    for i in range(m):
        matrix[i][0] = True
    for j in range(1, halfSumArr + 1):
        matrix[0][j] = arr[0] == j
    for i in range(1, m):
        for j in range(1, halfSumArr + 1):
            if matrix[i - 1][j]:
                matrix[i][j] = matrix[i - 1][j]
            elif j >= arr[i]:
                matrix[i][j] = matrix[i - 1][j - arr[i]]
    return matrix[i - 1][halfSumArr]


print(solved(arr, m, sum(arr)))