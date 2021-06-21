
def find_result(s, n, sum):
    #base
    if (sum == 0):
        return True
    if (n == 0):
        return False

    if (s[n - 1] > sum):
        return find_result(s, n - 1, sum)
 
    return find_result(s, n-1, sum) or find_result(s, n-1, sum-s[n-1])


if __name__ == '__main__':
    n = int(input())
    s = list(map(int, input().split()))

    if (sum(s) % 2 != 0):
        print ("False")
    else:
        print (find_result(s, n, sum(s)/2))