lines = ''
while True:
    try:
        s = input()
        if s and lines:
            lines = lines + '\n' + s
        elif s and len(lines) == 0:
            lines = lines + s
        else:
            break
    except:
        lines = lines + '\n'
        break

for c in lines:
    if c == '\n':
        print('\n', end='')
    else:
        print(chr(ord(c)-7), end='')