t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    
    pre = [0]*15
    for i in range(1,15):
        pre[i] = i
    for _ in range(1,k+1):
        now = [0]*15
        for i in range(1,n+1):
            for j in range(1,i+1):
                now[i] += pre[j]
        pre = now
    print(now[n])
            
