num=1000000
a = [False,False] + [True]*(num-1)
primes=[]

for i in range(2,num+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, num+1, i):
            a[j] = False

while True:
    count = 0
    n = int(input())
    if n == 0:
        break
    for i in range(n+1,2*n+1):
        if a[i] == True:
            count += 1
    print(count)
