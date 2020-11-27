n,m = map(int,input().split())

board = []*n

for _ in range(n):
    board.append(input())
mini = 65
for i in range(n-7):
    for j in range(m-7):
        cnt_w = 0
        cnt_b = 0
        start = 'W'
        now = start
        for k in range(i,i+8):
            for l in range(j,j+8):
                if board[k][l] != now:
                    cnt_w += 1
                if l == j+7:
                    continue
                if now == 'W':
                    now = 'B'
                    continue
                if now == 'B':
                    now = 'W'
                    continue
        start = 'B'
        now = start
        for k in range(i,i+8):
            for l in range(j,j+8):
                if board[k][l] != now:
                    cnt_b += 1
                if l == j+7:
                    continue
                if now == 'W':
                    now = 'B'
                    continue
                if now == 'B':
                    now = 'W'
                    continue
        temp = 0
        if cnt_w > cnt_b:
            temp = cnt_b
        else:
            temp = cnt_w
        if mini > temp:
            mini = temp
print(mini)
