raw_array = [3,4,1,5,1,2,7,8,9,10,4,6,22,17,16,13,18, 26, 25, 24, 21]

import time
start = time.time()

def insersion_sort(array):
    min_index = 0
    while min_index < (len(array)-1):
        current_index = min_index
        while current_index >= 0:
            if (array[current_index +1] < array[current_index]):
                array[current_index], array[current_index+1] = array[current_index+1], array[current_index]
            current_index -= 1
        min_index += 1
    return array
            
array = [i for i in raw_array]
sorted_array = insersion_sort(array)
print(raw_array)
print(sorted_array)
print('\nRun Time : {0:.10f}'.format(time.time() - start))