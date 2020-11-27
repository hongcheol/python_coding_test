S = input()

alpha = [-1]*26

for i in range(len(S)):
    if alpha[ord(S[i])-97] == -1:
        alpha[ord(S[i])-97] = i
for data in alpha:
    print(data,end=' ')
