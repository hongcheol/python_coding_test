n = int(input())
temp = 0

if n%2 == 0:
    for i in range(2*n):
        star = ''
        if i%2 == 1:
            star += ' '
        for j in range(n-1):
            if j%2 == 0:
                star += '*'
            else:
                star += ' '
        print(star)
        
else:
    for i in range(2*n):
        star = ''
        temp = n
        if i%2 == 1:
            star += ' '
            temp = n-2
        for j in range(temp):
            if j%2 == 0:
                star += '*'
            else:
                star += ' '
        print(star)
