numbers = [3, 7, 2, 9, 5]

def get_min_max(numbers):

    min_val = numbers[0]
    max_val = numbers[0]

    for n in numbers:
        if n > max_val:
            max_val = n
        if n < min_val:
            min_val = n
    return max_val, min_val

max_val, min_val = get_min_max(numbers)


print("최대값:", max_val)
print("최소값:", min_val)