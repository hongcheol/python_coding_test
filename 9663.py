def promising(i):
    k = 1
    global col
    switch = True
    while k<i and switch:
        if col[i] == col[k] or abs(col[i]-col[k]) == i-k:
            switch = False
        k += 1
    return switch

def queen(idx):
    j = 0
    global n
    global col
    global cnt
    if idx == n:
        cnt += 1
    else:
        for j in range(1,n+1):
            col[idx+1] = j
            queen(idx+1)
    
n = int(input())
col = [0] * (n+1)
cnt = 0
ans = []
queen(1)
print(ans)
