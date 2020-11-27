import math
for j in range(int(input())):
    x, y = map(int,input().split())
    n = int(math.sqrt(y-x))
    ans = 2*n - 1
    
    temp = y-x-n**2#가고 남은 거리
    i = n
    while temp != 0:
        if temp//i >= 0:
            ans += temp//i
            temp %= i
        i -= 1
        if i == 0:
            break
    
    print(ans)
