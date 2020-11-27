string = input()
string = string.upper()
answer = ''
alpha = [0]*26
for i in range(len(string)):
    alpha[ord(string[i])-65] += 1
most = -1
most_posi = -1
for i in range(26):
    if alpha[i] > most:
        most = alpha[i]
        most_posi = i
    elif alpha[i] == most and most_posi != -1:
        most_posi = 100

    else:
        continue

if most_posi == 100:
    print('?')
else:
    print(chr(most_posi + 65))
