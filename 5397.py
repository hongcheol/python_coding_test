t = int(input())
for j in range(0,t):
    left = []
    right = []
    key = input()
    for i in key:
        if i == '-':
            if left:
                left.pop()
        elif i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        else:
            left.append(i)
    left.extend(reversed(right))
    print(''.join(left))
        
