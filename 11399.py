n = int(input())
man = list(map(int,input().split()))
man.sort()
ans = 0
for i in range(n,0,-1):
    ans += man[n-i]*i
print(ans)
