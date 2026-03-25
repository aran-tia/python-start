def get_number_total(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
    
    total = 0

    for v in count.values():
        if v >= 2:
            total += v

    return total


numbers = [1, 2, 2, 3, 3, 4, 4, 5]
print(get_number_total(numbers))