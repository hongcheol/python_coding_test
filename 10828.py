import sys

n = int(input())
stack = []
top = 0
for _ in range(n):
    array = list(map(str,sys.stdin.readline().split()))
    if array[0] == 'push':
        stack.append(int(array[1]))
        top += 1
        
    if array[0] == 'pop':
        if top == 0:
            print(-1)
        else:
            print(stack.pop(-1))
            top -= 1
            
    if array[0] == 'top':
        if top == 0:
            print(-1)
        else:
            print(stack[top-1])
            
    if array[0] == 'empty':
        if top == 0:
            print(1)
        else:
            print(0)

    if array[0] == 'size':
        print(top)
