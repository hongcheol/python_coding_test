def combi(cnt):
    if cnt == m:
        for j in range(m):
            print(answer[j],end=' ')
        print()
        return
    for i in range(1,n+1):
        if cnt != 0:
            if answer[cnt-1] > i:
                continue
        answer[cnt] = i
        combi(cnt+1)

n,m = map(int,input().split())
visit = [False]*9
answer = [0]*10
combi(0)
