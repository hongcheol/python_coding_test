n = int(input())
paper = []
answer = [0,0,0]
def solve(x,y,n):
    global paper
    check = paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != paper[i][j]:
                solve(x,y,n//3)
                solve(x,y+n//3,n//3)
                solve(x,y+2*n//3,n//3)
                solve(x+n//3,y,n//3)
                solve(x+n//3,y+n//3,n//3)
                solve(x+n//3,y+2*n//3,n//3)
                solve(x+2*n//3,y,n//3)
                solve(x+2*n//3,y+n//3,n//3)
                solve(x+2*n//3,y+2*n//3,n//3)
                return
    answer[check+1] += 1
for i in range(n):
    paper.append(list(map(int,input().split())))

solve(0,0,n)
for data in answer:
    print(data)
