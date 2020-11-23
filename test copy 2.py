raw_array = [3,4,1,5,1,2,7,8,9,10,4,6,22,17,16,13,18, 26, 25, 24, 21]
max_heap = 0

import time
start = time.time()

def compare(parent, child):
    if max_heap:
        return (parent < child)
    else:
        return (parent > child)


def children(array, parent):
    left = parent*2
    right = parent*2+1
    if len(array)<=left:
        left = None
    if len(array)<=right:
        right = None
    return left, right


def heap_tree(array, parent):
    left, right = children(array, parent)
    top = parent

    if left and compare(array[top], array[left]):
        top = left
    if right and compare(array[top], array[right]):
        top = right
    
    if top != parent:
        array[top], array[parent] = array[parent], array[top]
        array = heap_tree(array, top)
        array = heap_tree(array, parent)
    return array


def heap_caller(array):
    array = [0]+array
    parent = len(array)//2
    for i in range(parent, 0, -1):
        array = heap_tree(array, i)
    
    print('heap_tree : ', array)
    sorted_array = [0]
    i=len(array)-1
    while (i>0):
        array[i], array[1] = array[1], array[i]
        sorted_array.append(array[i])
        array = heap_tree([array[i] for i in range(0, i)], 1)
        i -= 1
    return sorted_array


print('raw_array : ', raw_array)
array = [i for i in raw_array]
sorted_array = heap_caller(array)
print('sort_array :', sorted_array)

print('\nRun Time : {0:.10f}'.format(time.time() - start))