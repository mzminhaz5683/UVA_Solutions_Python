# recursion needs high time complexity

array_raw = [7,5,4,3,9,10,13,14]
target = 14

import time
start = time.time()

def binary_search(start, end):
        
    mid = (start + end)//2
    if (target == array[mid]) and (start <= end):
        index = mid
    elif (target < array[mid]) and (start <= end):
        index = binary_search(start, mid-1)
    elif (target > array[mid]) and (start <= end):
        index = binary_search(mid+1, end)
    else:
        index = None

    return index

# ascending
array = sorted(array_raw)
print(array_raw, '\nTarget : ', target)
index = binary_search(0, len(array)-1)
try:
    index + 1
    for i in range(0, len(array_raw)):
        if (array_raw[i] == array[index]):
            print('\nIndex : ', i)
            break
except:
    print('\nIndex : ', None)

print('\nTime : {0:.10f}'.format(time.time()-start))