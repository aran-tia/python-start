def count_even_duplicates(numbers):
    count = {}

    for n in numbers:
        if n % 2 == 0:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

    result = 0

    for v in count.values():
        if v >= 2:
            result += 1
    
    return result

numbers = [1, 2, 2, 3, 3, 4, 4, 5, 6]
print(count_even_duplicates(numbers))
