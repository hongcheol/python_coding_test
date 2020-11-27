t = int(input())
for _ in range(t):
    d = 0
    p = []*155
    inStart = set()
    inEnd = set()
    temp = set()
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    for _ in range(n):
        x, y, r = map(int,input().split())
        p.append(x)
        p.append(y)
        p.append(r)
    for i in range(0,n*3,3):
        d = (p[i]-x1)**2 + (p[i+1]-y1)**2
        if d < p[i+2]**2:
            inStart.add(i//3)
    for i in range(0,n*3,3):
        d = (p[i]-x2)**2 + (p[i+1]-y2)**2
        if d < p[i+2]**2:
            inEnd.add(i//3)
    temp = inStart
    inStart = inStart-inEnd
    inEnd = inEnd - temp
    print(len(inStart)+len(inEnd))
    del(p)
    del(inStart)
    del(inEnd)
