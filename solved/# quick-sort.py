raw_array = [3,4,1,5,1,2,7,8,9,10,4,6,22,17,16,13,18, 26, 25, 24, 21, 4,5,6,7,12,11,10,9,6]
#raw_array = [3,4,1,5,1,2]
import time
start = time.time()

def quick_sort(array):
    if (len(array) <= 1):
        return array
    else:
        i = len(array)-1
        pivort = array[i]
        pivort_min_array = []
        pivort_max_array = []
        for j in range(0, i):
            if (array[j] < pivort):
                pivort_min_array.append(array[j])
            else:
                pivort_max_array.append(array[j])

        sorted_min_array = quick_sort(pivort_min_array)
        sorted_max_array = quick_sort(pivort_max_array)

        sorted_min_array.append(pivort)
        array = sorted_min_array + sorted_max_array
    
        return array

array = [i for i in raw_array]
sorted_array = quick_sort(array)

print(raw_array)
print(sorted_array)

print('\nRun Time : {0:.10f}'.format(time.time() - start))