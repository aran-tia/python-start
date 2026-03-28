def get_duplcate_odd(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    result = []

    for k, v in count.items():
        if k % 2 == 1 and v >= 2:
            result.append(k)

    return result

numbers = [1, 2, 2, 3, 3, 4, 4, 4 ,5 ,6]
print(get_duplcate_odd(numbers))