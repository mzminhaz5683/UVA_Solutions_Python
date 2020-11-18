dicty = {}
while True:
    try:
        for c in input():
            if c in dicty:
                print(dicty[c], end='')
            elif c:
                x = chr(ord(c)-7)
                dicty[c] = x
                print(x, end='')
            else:
                break
        print('\n', end='')
    except:
        break