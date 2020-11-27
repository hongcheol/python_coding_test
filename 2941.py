import sys

string = sys.stdin.readline()
ans = 0
for i in range(len(string)-1):
    if string[i] == '=':
        if string[i-1] == 'c' or string[i-1] == 's' or string[i-1] == 'z':
            ans += 0
    elif string[i] == '-':
        if string[i-1] == 'c' or string[i-1] == 'd':
            ans += 0
    elif string[i] == 'j':
        if i == 0:
            ans += 1
        elif string[i-1] == 'l' or string[i-1] == 'n':
            ans += 0
        else:
            ans += 1
    elif string[i] == 'z':
        if i == 0:
            ans += 1
        elif string[i-1] == 'd':
            if i != len(string):
                if string[i+1] == '=':
                    ans += 0
                else:
                    ans += 1
            else:
                ans += 1
        else:
            ans += 1
    else:
        ans += 1
print(ans)
