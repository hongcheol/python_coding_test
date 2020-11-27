def isPrime(n):
    temp = int(n**0.5)+1
    if n != 1:
        for i in range(2,temp):
            if n%i == 0:
                return False
    else:
        return False
    
    return True

prime = []
array = []
n,k = map(int,input().split())
for i in range(2,n+1):
    if isPrime(i) == True:
        prime.append(i)
    array.append(i)

cnt = 0
while cnt < k:
    div = prime.pop(0)
    for i in range(len(array)):
        if array[i] == 0:
            continue
        
        if array[i] % div == 0:
            if cnt == k-1:
                print(array[i])
            array[i] = 0
            cnt += 1
