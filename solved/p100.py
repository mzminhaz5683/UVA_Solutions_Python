def cycle_finder(x):
    c = 0
    while x >= 1:
        c = c + 1
        if x == 1:
            return c
        elif x % 2 != 0:
            x = 3*x + 1
        elif x % 2 == 0:
            x = x/2
    return c

dictionary = {} # as have multi stack input set
while True:
    try:
        scan1, scan2 = input().split()
        i = int(scan1)
        j = int(scan2)
        if (i > j):
            i, j = j, i

        max_c = 0
        if (0<i and j<1000000):
            for x in range(i,j+1):

                if (x in dictionary):
                    c = dictionary[x]
                else:
                    c = cycle_finder(x)
                    dictionary[x] = c
                if (c>max_c):
                    max_c = c
        
        print('{0} {1} {2}'.format(scan1, scan2, max_c))
    except Exception as e:
        #print('except: ', e)
        break