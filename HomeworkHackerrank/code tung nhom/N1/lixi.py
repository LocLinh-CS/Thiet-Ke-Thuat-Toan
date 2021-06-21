n = int(input())
money = list(map(int, input().split()))
tong = 0
for i in money:
    tong = tong + i

if tong % 2 != 0:
    print(False)
else:
    tong2 = tong//2
    Matrix = [[False for x in range(0, tong2 +1 )] for y in range (0,len(money)) ]
    for i in range(0, n):
        Matrix[i][0] = True
    for j in range (1, tong2 +1):
        Matrix[0][j] = money[0] == j
    for i in range (1, n):
        for j in range (1, tong2+1):
            if Matrix[i - 1][j]:
                Matrix [i][j] = Matrix[i - 1][j]
            elif j >= money[i]:  
                Matrix[i][j] = Matrix[i - 1][j - money[i]]
    print (Matrix[i-1][tong2])
