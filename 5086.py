n = int(input())
temp = n
ran = int(n**0.5)
for i in range(2,n+1):
    
    if temp%i == 0:
        while temp%i == 0 and temp//i > 0:
            print(i)
            temp //= i
            
