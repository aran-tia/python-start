def count_numbers(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    return count

numbers = [1, 2, 2, 3, 3, 3, 4]

print(count_numbers(numbers))