def sum_unique_odd(numbers):
    count = {}

    for n in numbers:
        if n % 2 == 1:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
    
    result = 0

    for k, v in count.items():
        if v == 1:
            result += k
    
    return result

numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7]
print(sum_unique_odd(numbers))