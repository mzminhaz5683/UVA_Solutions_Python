import sys

lines = ''
s = sys.stdin.readline()
while True:
    try:
        if s == '\n':
            break
        elif s[-1] == '\n':
            lines = lines + s
            s = sys.stdin.readline()
        elif s[-1] != '\n':
            lines = lines + s
            break
    except:
        break

for c in lines:
    if c == '\n':
        print('\n', end='')
    else:
        print(chr(ord(c)-7), end='')