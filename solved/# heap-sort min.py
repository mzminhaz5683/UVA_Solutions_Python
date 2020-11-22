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

# min heap
def min_heap_tree(array, parent=1):
    left, right = child_finder(array, parent)
    smallest = parent

    if left and (array[left] < array[smallest]):
        smallest = left
    
    if right and (array[right] < array[smallest]):
        smallest = right
    
    if (smallest != parent):
        array[parent], array[smallest] = array[smallest], array[parent]
        array = min_heap_tree(array, smallest)

    return array


heap_array = [0]+[i for i in raw_array]

for i in range(len(heap_array)//2, 0, -1):
    heap_array = min_heap_tree(heap_array, i)

print(len(heap_array))
print(raw_array)
print(heap_array)

for i in range(len(heap_array)-1, 0, -1):
    heap_array[i], heap_array[1] = heap_array[1], heap_array[i]
    heap_array = min_heap_tree(heap_array, 1)

print(heap_array)

print('\nRun Time : {0:.10f}'.format(time.time() - start))