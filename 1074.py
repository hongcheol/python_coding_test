def z(n,x,y):
    global result
    if n == 2:
        if x == X and y == Y:
            print(result)
            return
        result += 1
        if x == X and y + 1 == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y + 1 == Y:
            print(result)
            return
        result += 1
        return
    z(n/2,x,y)
    z(n/2,x,y+ n/2)
    z(n/2,x+n/2,y)
    z(n/2,x+n/2,y+n/2)

result = 0    
n,X,Y = list(map(int,input().split(' ')))
z(2**n,0,0)
