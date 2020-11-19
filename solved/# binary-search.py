array_raw = [7,5,4,3,9,10,13]
target = 3

import time
start = time.time()

def binary_search(array, target):
    min_index = 0
    max_index = len(array)-1

    while(min_index <= max_index):
        mid = (min_index + max_index)//2
        if (target == array[mid]):
            return mid
        elif (target < array[mid]):
            max_index = mid -1
        elif (target > array[mid]):
            min_index = mid +1
    return None

# ascending
array = sorted(array_raw)
print(array_raw, '\nTarget : ', target)
index = binary_search(array, target)
try:
    index + 1
    for i in range(0, len(array_raw)):
        if (array_raw[i] == array[index]):
            print('\nIndex : ', i)
            break
except:
    print('\nIndex : ', None)

print('Time : {0:.10f}'.format(time.time()-start))