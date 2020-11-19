import time
start = time.time() # time

def linear_search(array, target):
    for i in range(0, len(array)):
        if (array[i] == target):
            return i
    return None

array = [4, 3, 19, 6, 8, 1, 17, 7, 8]
target = 17
print('\nIndex : ', linear_search(array, target))

print('\nTime : {0:.10f}'.format((time.time() - start))) # time