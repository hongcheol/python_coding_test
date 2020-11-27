dp = [1]

n = int(input())
num = 1
for i in range(n):
    dp.append(dp[i]*num)
    num += 1

cnt = 0
s = str(dp[n])
l = len(s)
for i in range(l-1,-1,-1):
    if s[i] == '0':
        cnt += 1
    else:
        break
print(cnt)

