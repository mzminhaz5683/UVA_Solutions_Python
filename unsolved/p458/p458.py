import sys
lines = ''

with open(sys.argv[1], 'r') as f:
    for string in f.readlines():
        lines = lines + string

for c in lines:
    try:
        if c == '\n':
            print('\n', end='')
        else:
            print(chr(ord(c)-7), end='')
    except Exception as e:
        continue