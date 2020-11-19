raw_array = [3,4,1,5,1,2,7,8,9,10,4,6,22,17,16,13,18, 26, 25, 24, 21]

import time
start = time.time()

# ascending
def bubble_sort(array):
    max_index = len(array)
    for i in range(0, max_index):
        for j in range(0, max_index-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
        max_index -= 1
    return array

array = [i for i in raw_array]
sorted_array = bubble_sort(array)
print(raw_array)
print(sorted_array)

print('\nRun Time : {0:.10f}'.format(time.time() - start))