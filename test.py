a = 18

def square_root(x):

    for i in range(x-1, 1, -1):
        if (i*i == x):
            return i
        elif (i*i < x):
            return '{0} + square_root({1})'.format(i, (x-(i*i)))
    
    return None

print(square_root(a))