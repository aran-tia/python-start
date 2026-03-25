def get_duplicate_numbers(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    result = []

    for k, v in count.items():
        if v >= 2:
            result.append(k)
    return result

numbers = [1, 2, 2, 3, 4, 4, 5]
print(get_duplicate_numbers(numbers))