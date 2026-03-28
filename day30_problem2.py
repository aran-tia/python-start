def get_least_duplicate(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    min_count = 99999
    min_num = 0

    for k, v in count.items():
        if v >= 2 and v < min_count:
            min_count = v
            min_num = k

    return min_num

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 6]
print(get_least_duplicate(numbers))