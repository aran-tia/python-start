def get_least_numbers(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    min_count = 99999

    for v in count.values():
        if v < min_count:
            min_count = v

    result = []

    for k, v in count.items():
        if v == min_count:
            result.append(k)
    
    return result

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]
print(get_least_numbers(numbers))
