def check(sum_target,n,arr):
    if(sum_target==0):
        return True
    if (n == 0 and sum_target != 0) :
        return False
    if (arr[n - 1] > sum_target) :
        return check(sum_target,n-1,arr) 
    return check(sum_target,n-1,arr) or check(sum_target-arr[n-1],n-1,arr)
n = int(input())
arr = list(map(int,input().split()))
sum_total = sum(arr)
sum_target = sum_total//2
sum_temp = 0
if(sum_total%2):
    print("False")
else:
    print(check(sum_target,n,arr))