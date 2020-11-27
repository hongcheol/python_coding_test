n,l = map(int,input().split())
imp = 0
while True:
    if n == 1:
        if l == 2:
            break
        else:
            imp = 1
            break
    if n/l == n//l:
        if (n/l)%l == 0:
            break
        else:
            l += 1

temp = n/l - l/2 + 1/2
temp = int(temp)
if imp == 1:
    print(-1)
else:
    for i in range(l-1):
        print(temp+i,end=' ')
    print(temp+l-1,end='')
