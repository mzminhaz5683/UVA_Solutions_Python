import sys
dicty = {}
while True:
    try:
        for c in sys.stdin.readline():
            if c in dicty:
                print(dicty[c], end='')
            elif c == '\n':
                print('\n', end='')
                break
            elif c:
                x = chr(ord(c)-7)
                dicty[c] = x
                print(x, end='')
            else:
                break
    except:
        break