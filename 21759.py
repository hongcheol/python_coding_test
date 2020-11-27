a, b = map(int,input().split())
if(b>a):
    a,b = b,a
while b != 0:
    a = a%b
    a,b = b,a
     
for _ in range(a):
    print(1,end='')
