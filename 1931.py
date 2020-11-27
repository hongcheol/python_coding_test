meet = []
ans = []
n = int(input())
for _ in range(n):
    s,e = map(int,input().split())
    meet.append([s,e])

fast_end_meet = sorted(meet,key = lambda x : [x[1],x[0]])

j = 0
ans.append(fast_end_meet[0])
for i in range(1,n):
    if fast_end_meet[i][0] >= fast_end_meet[j][1]:
        ans.append(fast_end_meet[j][1])
        j = i
print(len(ans))
    
        
