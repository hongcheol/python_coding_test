score = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
N, M = map(int,input().split())
n, m = map(str,input().split())

length = min(N,M)
couple = []
temp1 = [0]*(M+N)
temp2 = []*(M+N)
for i in range(length):
    couple.append(n[i])
    couple.append(m[i])
if N > M:
    for i in range(M,N):
        couple.append(n[i])
else:
    for i in range(N,M):
        couple.append(m[i])

for i in range(M+N):
    temp1[i] = score[ord(couple[i])-65]
for i in range(M+N-2):
     
    for j in range(M+N-i-1):
        temp1[j] = temp1[j] + temp1[j+1]
        if temp1[j] >= 10:
            temp1[j] -= 10
    
    
if temp1[0] != 0:
    print(str(temp1[0])+str(temp1[1])+"%")
else:
    print(str(temp1[1])+"%")
