def get_min_numbers(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    min_count = 99999
    min_num = 0

    for k, v in count.items():
        if v < min_count:
            min_count = v
            min_num = k
    return  min_num

numbers = [1, 2, 1, 3, 2, 1]

result = get_min_numbers(numbers)
print(result)