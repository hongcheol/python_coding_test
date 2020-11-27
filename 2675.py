t = int(input())

for _ in range(t):
    temp = list(map(str,input().split(' ')))
    for i in range(len(temp[1])):
        for _ in range(ord(temp[0])-ord('0')):
            print(temp[1][i],end='')
    print()
