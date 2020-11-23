linear_search = 0
binary_search = 0
selction_sort = 1

raw_array = [2,4,5,1,6,9,0,12,7]
target = 0

if linear_search:
    def linear_search_function(array, target):
        for i in range(0, len(array)):
            if (array[i] == target):
                return i
        return None

    array = [i for i in raw_array]
    print('array : ',raw_array, '\nTarget : ',target, '\nResult : ',linear_search_function(array, target))

if binary_search:
    def binary_search_function(array, target):
        i = -1
        max_index = len(array)-1
        while (i<(max_index-i)+1):
            i += 1
            #print('i = ', i)
            for j in range(0, max_index-i): # goes to (max_index-i)-1
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        print('Sort  : ', array)

        min_index = 0
        max_index = len(array)-1
        while min_index < max_index:
            mid_index = (min_index+max_index)//2
            if (target == array[mid_index]):
                return mid_index
            elif (target < array[mid_index]):
                max_index = mid_index
            elif (target >= array[mid_index]):
                min_index = mid_index
        return None

    array = [i for i in raw_array]
    print('array : ',raw_array)
    print('Target : ',target, '\nResult : ',binary_search_function(array, target))

if selction_sort:
    def selction_sort_function(array):
        for i in range(0, len(array)-1):
            smallest = i
            for j in range(i+1, len(array)):
                if array[j] < array[smallest]:
                    smallest = j
            if (smallest != i):
                array[smallest], array[i] = array[i], array[smallest]
        return array

    array = [i for i in raw_array]
    print('array : ',raw_array)
    print('Sort  : ',selction_sort_function(array))