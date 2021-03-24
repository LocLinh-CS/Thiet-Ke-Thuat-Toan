
def taobien(soluong, ngay):
    s1 = soluong
    s2 = soluong + soluong
    for i in range(ngay-2):
        s3 = ( s2**2 + soluong**2 ) / s1
        s1 = s2
        s2 = s3
    return s3

print(int(taobien(3,5)%1000000007))