dp = [0,1,2]

n = int(input())
if n == 1:
    print(1)
else:
    for i in range(2,n):
        dp.append((dp[i-1]+dp[i])%15746)

    print(dp[-1])
