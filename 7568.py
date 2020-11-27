import sys

n = int(sys.stdin.readline())
pool = []
for _ in range(n):
    man = list(map(int,sys.stdin.readline().split()))
    pool.append(man)

answer = []
for i in range(n):
    count = 1
    for j in range(n):
        if i == j:
            continue
        else:
            if pool[i][0] < pool[j][0] and pool[i][1] < pool[j][1]:
                count += 1
    answer.append(count)
print(' '.join(map(str,answer)))
