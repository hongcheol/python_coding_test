n = int(input())

cnt = 1
ans = 0
while n != 0:
    if n - cnt > 0:
        n -= cnt
        cnt += 1
        ans += 1
    elif n - cnt < 0:
        cnt = 1
    else:
        n -= cnt
        ans += 1

print(ans)
