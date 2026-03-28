def get_sum_even(numbers):
    count = {}

    for n in numbers:
        if n % 2 == 0:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

    result = 0

    for k, v in count.items():
        if v >= 2:
            result += v

    return result

numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6]
print(get_sum_even(numbers))

    