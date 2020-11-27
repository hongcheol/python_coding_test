import copy

n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

rcnt = 0
lcnt = 0
rmax = 0
lmax = 0

for i in range(n):
    if array[i] > lmax:
        lcnt += 1
        lmax = array[i]
    if array[n-i-1] > rmax:
        rcnt += 1
        rmax = array[n-i-1]

print(lcnt)
print(rcnt)
