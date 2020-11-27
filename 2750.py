n = int(input())

arr = []

for _ in range(n):
    i = int(input())
    arr.append(i)


arr.sort()
for i in range(0,n):
    print(arr[i])
