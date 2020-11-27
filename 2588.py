a = int(input())
b = int(input())

result = a*b

while b > 0:
    print(a*(b%10))
    b /= 10
    b = int(b)
print(result)
