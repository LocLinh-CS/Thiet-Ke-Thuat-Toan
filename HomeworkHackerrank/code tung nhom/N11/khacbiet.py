def find(a,n,idx, tempA):
    global minS
    if idx == n:
        tempMinS= max(tempA) - min(tempA)
        if tempMinS  < minS:
            minS= tempMinS
        return
    for i in a[idx]:
        tempA.append(i)
        find(a,n,idx+1,tempA)
        tempA.pop()

n= int(input())
a=[]
minS=10000000
tempA=[]
for i in range(n):
    a.append(list(map(int, input().split())))

find(a,n,0,tempA)
print(minS)