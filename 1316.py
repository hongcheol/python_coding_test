t = int(input())
ans = 0
for _ in range(t):
    alpha = [0]*26
    string = input()
    l = len(string)
    pos = 0
    for i in range(l):
        j = ord(string[i])-97
        if alpha[j] == 0:
            alpha[j] += 1
            continue
        elif alpha[j] > 0:
            if string[i] != string[i-1]:
                pos = 1
                break
    if pos == 0:
        ans += 1
print(ans)
