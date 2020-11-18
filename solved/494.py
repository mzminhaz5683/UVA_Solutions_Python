def counter(string):
    words = string.split()
    counter = 0
    for word in words:
        local_counter = 0
        c_fiag = 0
        for c in word:
            if ((65<= ord(c) <=90) or (97<= ord(c) <=122)):
                if c_fiag == 0:
                    local_counter += 1
                c_fiag = 1
            else:
                c_fiag = 0
        counter += local_counter   
    return counter

lines = []
while True:
    try:
        string =input()
        if string:
            lines.append(counter(string))
        else:
            break
    except:
        break

for number in lines:
    print(number)

