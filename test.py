raw_array = [0,7,5,4,3,7,6,5,1]

def child_finder(array, parent):
    left = parent * 2
    right = parent * 2 + 1
    if (len(array) <= left):
        left = None
    if (len(array) <= right):
        right = None
    return left, right
    

def heap_tree(array, parent):
    left, right = child_finder(array, parent)
    smallest = parent

    if left and array[smallest] > array[left]:
        smallest = left
    if right and array[smallest] > array[right]:
        smallest = right

    if smallest != parent:
        array[parent], array[smallest] = array[smallest], array[parent]
        array = heap_tree(array, smallest)
    return array

array = [i for i in raw_array]
for i in range(len(array)//2, 0, -1):
    array = heap_tree(array, i)

print(raw_array)
print(array)
