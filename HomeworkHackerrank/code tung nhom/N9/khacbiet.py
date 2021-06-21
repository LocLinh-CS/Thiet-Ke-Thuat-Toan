n = int(input())
a = []
for i in range(n) :
    a.append(list(map(int,input().split())))

pos = [0] * n
ma = mi = a[0][0]
size = [0] * n
for i in range(n) :
    size[i] = len(a[i])

total_size = sum(size) 
ans = 1000000009

for idx in range(min(size)) :
    for j in range(n) :
        pos[j] = max(pos[j],idx)

    mi = ma = a[0][pos[0]]
    for i in range(n) :
            ma = max(ma,a[i][pos[i]])
            mi = min(mi,a[i][pos[i]])

    for i in range(n) :
        while (pos[i] + 1 < size[i] and a[i][pos[i]] < ma) :
            pos[i] += 1

    mi = ma = a[0][pos[0]]
    
    for i in range(n) :
        ma = max(ma,a[i][pos[i]])
        mi = min(mi,a[i][pos[i]])

    ans = min(ans,ma-mi)
    
    if sum(pos) >= total_size - n : break

print(ans)
        