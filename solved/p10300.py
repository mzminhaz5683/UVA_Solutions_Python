max = 100000
try:
    n = int(input())
    while n and (0<= n <=max):
        f = int(input())
        budget = 0
        while f and (0<= f <=max):
            area, animal, firendly = input().split()
            area = int(area)
            animal = int(animal)
            firendly = int(firendly)
            if ((0<= area <=max) and (0<= animal <=max) and (0<= firendly <=max)):
                budget = budget + ((area/animal)*firendly)*animal
            f = f - 1
        print(round(budget))
        n = n - 1
except:
    pass