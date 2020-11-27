import sys
t = int(input())

for _ in range(t):
    s = sys.stdin.readline().rstrip()
    stack = []
    VPS = True
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if stack == []:
                sys.stdout.write('NO\n')
                VPS = False
                break
            else:
                stack.pop()
    if stack != []:
        sys.stdout.write('NO\n')
    else:
        if VPS == True:
            sys.stdout.write('YES\n')
