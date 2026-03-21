def get_second_number(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    max1_num = 0
    max1_count = 0
    max2_num = 0
    max2_count = 0
    
    for k, v in count.items():
        if v > max1_count:
            max2_count = max1_count
            max2_num = max1_num

            max1_count = v
            max1_num = k
        
        elif v > max2_count:
            max2_count = v
            max2_num = k

    return max1_num, max2_num

numbers = [1, 2, 1, 3, 2, 1]
result = get_second_number(numbers)
print(result)
