'''UVA :: 10071 - Back to High School Physics'''
while True:
    try:
        scan1, scan2 = input().split()
        v=int(scan1)
        t=int(scan2)
        if ( -100 <= v <= 100) and (0 <= t <= 200):
            print(v*2*t)
    except:
        break