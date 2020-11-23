a = 18

def square_root_tree(x):
    array = []
    break_point = 0
    for i in range(2, x):
        for j in range(2, x):
            if (i * j == x):
                array.append(i)
                #print('x, i, j : ', x, i, j)
                array += square_root_tree(j)
                break_point = 1
                break
        if break_point:
            break
    
    if break_point == 0:
        array.append(x)
    return array

def square_root(a):
    array = square_root_tree(a)
    single = []
    double = []
    already_checked = []
    for i in range(0,len(array)):
        counter = 0
        if array[i] in already_checked:
            continue
        else:
            already_checked.append(array[i])
            for j in range(0, len(array)):
                if array[i] == array[j]:
                    counter += 1
                    if counter == 2:
                        double.append(array[i])
                        counter = 0
            if counter==1:
                single.append(array[i])
    
    double_values = 1
    for i in double:
        double_values *= i
    
    single_values = 1
    for i in single:
        single_values *= i
    
    if single_values > 1:
        return '{0} * square_root({1})'.format(double_values, single_values)
    return double_values


print('Target = ',a, '\n', square_root(a))