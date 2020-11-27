import math
N = int(input())
array = []
total = 0
count = [0]*8010
for i in range(N):
    array.append(int(input()))
    total += array[i]

array.sort()
print(round(total/N))
print(array[N//2])
temp = 0
for i in range(N):
    count[array[i]+4000] += 1

maximum = max(count)
idx = 0
ans = 0
while True:
    if count[idx] == maximum:
        if temp == 1:
            ans = idx - 4000
            break
        else:
            ans = idx - 4000
            temp += 1
    if idx == array[-1] + 4000:
        break
    idx += 1

print(ans)
print(array[-1]-array[0])
