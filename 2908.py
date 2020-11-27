import sys
num = list(map(str,sys.stdin.readline().split()))

a = num[0][::-1]
b = num[1][::-1]
if a>b:
    print(a)
else:
    print(b)
