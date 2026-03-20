numbers = [3, 7, 2, 9, 5]



def get_max(numbers):

    max_val = numbers[0]

    for n in numbers:
        if n > max_val:
            max_val = n

    return max_val

result = get_max(numbers)

print(result)