def get_max_number(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
        
    max_count = 0
    max_num = 0

    for k, v in count.items():
        if v > max_count:
            max_count = v
            max_num = k
    return max_num

result = get_max_number(numbers)

print(result)