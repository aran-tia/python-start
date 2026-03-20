numbers = [1, 2, 3, 4, 5, 6]


def sum_even(numbers):
    total = 0
    for n in numbers:
        if n % 2 == 0:
            total += n

    return total

result = sum_even(numbers)
print(result)