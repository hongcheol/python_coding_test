n , lst = int(input()),list(map(int,input().split()))
hap = 0
temp = 0
for i in range(n):
    temp = lst[i]*(i+1)
    print(temp-hap,end = ' ')
    hap += temp - hap
    
