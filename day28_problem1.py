def count_unique(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    result = []

    for k, v in count.items():
        if v == 1:
            result.append(k)

    return len(result)

numbers = [1, 2, 2, 3, 3, 4, 5, 5]
print(count_unique(numbers))


