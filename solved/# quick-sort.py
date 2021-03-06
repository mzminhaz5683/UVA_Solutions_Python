raw_array = [3,4,1,5,1,2,7,8,9,10,4,6,22,17,16,13,18, 26, 25, 24, 21, 4,5,6,7,12,11,10,9,6]
#raw_array = [3,4,1,5,1,2]
import time
start = time.time()

def quick_sort(array):
    pivort = len(array)-1
    lowers = []
    highers = []
    for i in range(0, pivort):
        if (array[i] < array[pivort]):
            lowers.append(array[i])
        else:
            highers.append(array[i])
    
    if len(lowers) > 1:
        lowers = quick_sort(lowers)
    if len(highers) > 1:
        highers = quick_sort(highers)

    return lowers+[array[pivort]]+highers


array = [i for i in raw_array]
sorted_array = quick_sort(array)

print(raw_array)
print(sorted_array)

print('\nRun Time : {0:.10f}'.format(time.time() - start))