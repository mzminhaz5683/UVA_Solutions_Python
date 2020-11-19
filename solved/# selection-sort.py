raw_array = [3,2,4,1,6,7,2,1,0, 15, 20, 38, 5, 8, 10, 9]

import time
start = time.time()

# ascending
def selection_sort(array):
    for i in range(0, len(array)-1):
        smallest = i
        for j in range (i+1, len(array)):
            if (array[smallest]>array[j]):
                smallest = j
        if (smallest != i):
            array[i], array[smallest] = array[smallest], array[i]
    return array

print(raw_array)
sorted_array = selection_sort(raw_array)
print(sorted_array)

print('\nTime : {0:.10f}'.format(time.time() - start))

            