import sys
t = int(input())
for _ in range(t):
    score = 0
    relay = 0
    string = sys.stdin.readline()
    for i in range(len(string)):
        if string[i] == 'O':
            relay += 1
            score += relay
        else:
            relay = 0
    print(score)
