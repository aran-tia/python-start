numbers = [1, 2, 3, 4]

def get_sum(numbers):
    total = 0

    for n in numbers:
        total += n

    return total

result = get_sum(numbers)
print(result)