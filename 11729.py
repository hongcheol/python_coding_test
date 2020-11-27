
def move(start,end):
    print(start,end)
    
def hanoi(n,start,by,end):
    if n == 1:
        move(start,end)
    else:
        hanoi(n-1,start,end,by)
        move(start,end)
        hanoi(n-1,by,start,end)

n = int(input())
print(2**n-1)
hanoi(n,1,2,3)
