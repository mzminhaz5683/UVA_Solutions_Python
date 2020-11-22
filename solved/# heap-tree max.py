#raw_array = [3,4,1,5,1,2,7,8,9,10,4,6,22,17,16,13,18, 26, 25, 24, 21]
raw_array = [7,5,4,10,12,17,13,11,5]

import time
start = time.time()

def child_finder( array, parent):
    left_child = parent*2
    right_child = parent*2+1
    if (left_child >= len(array)):
        left_child = None
    if (right_child >= len(array)):
        right_child = None
    return left_child, right_child

# Max heap
def max_heap_tree(array, parent=1):
    left, right = child_finder(array, parent)
    largest = parent

    if left and (array[left] > array[largest]):
        largest = left
    
    if right and (array[right] > array[largest]):
        largest = right
    
    if (largest != parent):
        array[parent], array[largest] = array[largest], array[parent]
        array = max_heap_tree(array, largest)

    return array


heap_array = [0]+[i for i in raw_array]

for i in range(len(heap_array)//2, 0, -1):
    heap_array = max_heap_tree(heap_array, i)

heap_array.pop(0)
print(len(heap_array))
print(raw_array)
print(heap_array)


print('\nRun Time : {0:.10f}'.format(time.time() - start))