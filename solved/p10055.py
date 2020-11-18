while True:
    try:
        scan1, scan2 = input().split()
        print(abs(int(scan1) - int(scan2)))
    except:
        break