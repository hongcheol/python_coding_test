t = int(input())

for i in range(0,t):
    k = 0
    n,m = list(map(int, input().split(' ')))
    q = list((map(int, input().split(' '))))
    q = [(k, index) for index, k in enumerate(q)]
    
    count = 0
    temp = 0
    while len(q) != 0:
        j = 0
        while j < len(q):
            if(q[0][0] < q[j][0]):
                temp = q[0]
                del q[0]
                q.append(temp)
                j = 0
            else:
                j += 1
        
        count += 1
        if(q[0][1] == m):
            print(count)
        del q[0]
    
