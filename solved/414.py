input_list = []
while True:
    try:
        rows = int(input())
        a_set_counter = []
        for i in range(0, rows):
            flag = 0
            a_row_counter = 0
            for c in input():
                if c == ' ':
                    flag = 1
                else:
                    flag = 0
                if flag:
                    a_row_counter += 1
            a_set_counter.append(a_row_counter)
        input_list.append(a_set_counter)
    except Exception as e:
        #print(e)
        break

length = len(input_list)
length_count = 0
for a_set in input_list:
    length_count += 1
    try:
        min_value = min(a_set)
    except:
        min_value = 0
    sum_set = 0
    for value in a_set:
        sum_set += (value - min_value)
    
    if length_count != length:
        print(sum_set)
    elif sum_set:
        print(sum_set)