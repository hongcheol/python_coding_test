n = int(input())
def check(n):
    sub = n
    while n > 0:
        sub += n%10
        n //= 10
    return sub
array = []
for answer in range(n+1):
    if n == check(answer):
        array.append(answer)

if array == []:
    print(0)
else:
    print(array[0])
        
