def star(n,x,y):
    if n == 1:
        star_field[x][y] = '*'
    else:
        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    star(n//3,x+(n//3)*i,y+(n//3)*j)
n = int(input())
star_field = [[' ']*n for _ in range(n)]
star(n,0,0)
for data in star_field:
    print(''.join(data))
