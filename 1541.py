import sys

poly = list(map(str,sys.stdin.readline().split('-')))
num = []
for data in poly:
    hap = list(map(int,data.split('+')))
    result = 0
    for number in hap:
        result += number
    num.append(result)
ans = 0
for i in range(len(num)):
    if i == 0:
        ans += num[i]
    else:
        ans -= num[i]

print(ans)
     
