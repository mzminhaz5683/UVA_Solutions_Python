import sys
lines = ''
while True:
    try:
        s = sys.stdin.readline()
        if len(s) > 1:
            lines = lines + s
        else:
            break
    except:
        break

for c in lines:
    if c == '\n':
        print('\n', end='')
    else:
        print(chr(ord(c)-7), end='')