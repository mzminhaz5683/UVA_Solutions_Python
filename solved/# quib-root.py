a = 120

def fraction_tree(a):
    array = []
    breakpoint = 0
    for i in range(2, a):
        for j in range(2, a):
            if (i*j == a):
                array.append(i)
                array += fraction_tree(j)
                breakpoint = 1
                break
        if breakpoint:
            break
    
    if len(array) < 1:
        array.append(a)

    return array

def quib_root(a):
    array = fraction_tree(a)
    quib = 1
    others = 1
    checked = []
    for i in range(0, len(array)):
        if array[i] in checked:
            continue
        else:
            counter = 0
            checked.append(array[i])
            for j in range(0, len(array)):
                if array[i] == array[j]:
                    counter += 1
                if counter == 3:
                    quib *= array[i]
                    counter = 0
            if counter:
                others *= array[i]
    
    if others > 1:
        return '{0} * quib_root({1})'.format(quib, others)
    return quib


print('Target = ',a, '\n', quib_root(a))