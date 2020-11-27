num = [1]*10001
def d(n):
    temp = n
    ans = n
    while temp>0:
        ans += temp%10
        temp //= 10
    if ans > 10000:
        return 
    num[ans] = 0
    d(ans)

for i in range(1,len(num)):
    if num[i] == 1:
        d(i)
for i in range(1,len(num)):
    if num[i] == 1:
        print(i)
