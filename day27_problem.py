def get_max_count(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    max_count = 0

    for v in count:
        if v > max_count:
            max_count = v

    for v in count.values():
        if v == max_count:
            max_count = v

    return max_count

numbers = [1, 2, 2, 3, 3, 3, 4, 5]
print(get_max_count(numbers))