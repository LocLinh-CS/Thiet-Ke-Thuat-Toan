n = input()
a = sum([int(x) for x in input().split()])
print("False" if (a % 2 == 1 or a <= 0) else "True")