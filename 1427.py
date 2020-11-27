n = int(input())
arr = []
while int(n) > 0:
    arr.append(n%10)
    n = int(n/10)

arr.sort()
ans = 0
l = len(arr)
ten = 1
for i in range(l):
    ans += arr[i]*ten
    ten *= 10

print(ans)
