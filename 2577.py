a = int(input())
b = int(input())
c = int(input())
num = [0]*10
result = a*b*c
while result > 0:
    i = result%10
    num[i] +=1
    result //= 10
for i in range(10):
    print(num[i])
    
