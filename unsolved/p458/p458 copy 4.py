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
        break

dictionary = {}
for c in lines:
    if c == '\n':
        print('\n', end='')
    else:
        if c in dictionary:
            print(dictionary[c], end='')
        else:
            dictionary[c] = chr(ord(c)-7)
            print(dictionary[c], end='')