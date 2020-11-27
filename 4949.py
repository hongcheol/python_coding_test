import sys

while True:
    s = sys.stdin.readline().rstrip()
    if s == '.':
        break
    stack = []
    VPS = True
    for char in s:
        if char == '(':
            stack.append(char)
        if char == '[':
            stack.append(char)
        if char == ')':
            if stack == []:
                VPS = False
                break
            else:
                if stack[-1] == '[':
                    VPS = False
                    break
                else:
                    stack.pop()
        if char == ']':
            if stack == []:
                VPS = False
                break
            else:
                if stack[-1] == '(':
                    VPS = False
                    break
                else:
                    stack.pop()
    if VPS == True:
        if stack == []:
            sys.stdout.write('yes\n')
        else:
            sys.stdout.write('no\n')
    else:
        sys.stdout.write('no\n')
