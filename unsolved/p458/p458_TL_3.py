lines = input()
while True:
    try:
        lines = lines + '\n' + input()
    except:
#        lines = lines + '\n'
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