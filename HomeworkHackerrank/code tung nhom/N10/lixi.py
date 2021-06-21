n = int(input())
arr = list(map(int,input().split()))
res = -1
if sum(arr) % 2 != 0:
    res = 0
else:
    i = j = 0
    res = sum(arr) / 2
    tem = 0
    while((i!=len(arr)-1 and j!=len(arr)-1) and res!=1):
        if tem < res:
            tem = tem + arr[j]
            j = j + 1
        elif tem > res:
            tem = tem - arr[i]
            i = i + 1
        else:
            res = 1
print(res==1)