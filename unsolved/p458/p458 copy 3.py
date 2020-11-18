dictionary = {}
def decoder(lines):
    for c in lines:
        if c in dictionary:
            print(dictionary[c], end='')
        else:
            dictionary[c] = chr(ord(c)-7)
            print(dictionary[c], end='')


s1 = input()
while True:
    try:
        s2 = input()
        decoder(s1)
        print('\n', end='')
        s1 = s2
    except:
        decoder(s1)
        print('\n', end='')
        break
