raw_array = [3,4,1,5,1,2,7,8,9,10,4,6,22,17,16,13,18, 26, 25, 24, 21]

import time
start = time.time()

def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        mid = len(array)//2
        left_wind = merge_sort([array[i] for i in range(0, mid)])
        right_wind = merge_sort([array[i] for i in range(mid, len(array))])
        
        sorted_array = []
        left_min = 0
        right_min = 0
        while (left_min < len(left_wind) and (right_min < len(right_wind))):
            if (left_wind[left_min] < right_wind[right_min]):
                sorted_array.append(left_wind[left_min])
                left_min += 1
            else:
                sorted_array.append(right_wind[right_min])
                right_min += 1
        
        if (left_min == len(left_wind)):
            rest_of_array = [right_wind[i] for i in range(right_min, len(right_wind))]
        else:
            rest_of_array = [left_wind[i] for i in range(left_min, len(left_wind))]
        for i in rest_of_array:
            sorted_array.append(i)

    return sorted_array


array = [i for i in raw_array]
sorted_array = merge_sort(array)
print(raw_array)
print(sorted_array)


print('\nRun Time : {0:.10f}'.format(time.time() - start))