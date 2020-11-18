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

dictionary = {'\n':'\n'}
for c in lines:
    if c in dictionary:
        print(dictionary[c], end='')
    else:
        dictionary[c] = chr(ord(c)-7)
        print(dictionary[c], end='')