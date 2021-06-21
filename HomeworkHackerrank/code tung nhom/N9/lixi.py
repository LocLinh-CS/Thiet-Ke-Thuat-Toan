n = int(input())
arr = list(map(int,input().split()))
s = sum(arr)
if s&1 :
    print ("False")
    exit()

f = [0] * (s+1)
f[0] = 1

for a in arr :
    val = s
    while val - a >= 0 :
        f[val] = f[val - a]
        val -= 1
if f[s] == 1 :
    print("True") 
else :
    print("False")

