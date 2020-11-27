array = [0]*42
for _ in range(10):
    num = int(input())
    array[num%42] += 1

cnt = 0

for data in array:
    if data != 0:
        cnt += 1

print(cnt)
