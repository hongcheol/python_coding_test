n = int(input())

rooms = list(map(int,input().split()))
b, c = map(int,input().split())

mini = 0

for room in rooms:
    mini += 1
    room -= b
    if room > 0:
        mini += room//c
        if room%c != 0:
            mini += 1
print(mini)
