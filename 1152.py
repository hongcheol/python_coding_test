import sys

string = list(map(str,sys.stdin.readline().split(' ')))

ans = len(string)
if string[0] == '':
    ans -= 1
if string[-1] == '\n':
    ans -= 1
print(ans)
    
