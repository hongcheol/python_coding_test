import sys
t = int(input())

for _ in range(t):
    avg = 0
    count = 0
    ban = list(map(int,sys.stdin.readline().split()))
    for i in range(1,ban[0]+1):
        avg += ban[i]
    avg /= ban[0]
    for i in range(1,ban[0]+1):
        if avg < ban[i]:
            count+=1
    ans = (count/ban[0])*100
    print("%.3f%%"%(ans))
