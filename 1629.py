a,b,c = map(int,input().split())
answer = 1
def jae(a,b):
    if b == 0:
        return 0
    elif b == 1:
        return a%c
    elif b%2 == 1:
        return jae(a,b-1)*a
    temp = jae(a,b//2)
    temp %= c
    return temp**2%c

print(jae(a,b)%c)
