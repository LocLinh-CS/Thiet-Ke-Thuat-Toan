from bisect import bisect

n = int(input())
a = []
for x in range(n):
    a.append( [int(x) for x in input().split()])

def getSmallestDiff(a):
    numlist = []
    for i,l in enumerate(a):
        if not l:
            return []
        idx = bisect(numlist,(l[0],0))
        numlist.insert(idx,(l.pop(0),i))
    
    res = []
    res_range = float('inf')
    while a:
        min_val = numlist[0][0]
        min_idx = numlist[0][1]
        max_val = numlist[-1][0]
        if max_val - min_val < res_range:
            res_range = max_val - min_val
            res = [min_val,max_val]
        
        numlist.pop(0)
        l = a[min_idx]
        if not l:
            break
        idx = bisect(numlist,(l[0],0))
        numlist.insert(idx,(l.pop(0),min_idx))
    return max(res) - min(res)
            
print(getSmallestDiff(a))