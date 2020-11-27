x, y = 0,0
x_dot = [0]*1001
y_dot = [0]*1001
x_pos = list()
y_pos = list()
for _ in range(3):
    a,b = map(int,input().split())
    
    if x_dot[a] == 0:
        x_pos.append(a)
    if y_dot[b] == 0:
        y_pos.append(b)
    x_dot[a] += 1
    y_dot[b] += 1

if x_dot[x_pos[0]] != 2:
    print(x_pos[0],end= ' ')
else:
    print(x_pos[1],end= ' ')

if y_dot[y_pos[0]] != 2:
    print(y_pos[0])
else:
    print(y_pos[1])
