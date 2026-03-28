def get_most_even(numbers):
    count = {}

    for n in numbers:
        if n % 2 == 0:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

    max_count = 0
   
    for v in count.values():
        if v > max_count:
            max_count = v

    result = []

    for k, v in count.items():
        if v == max_count:
            result.append(k)
    
    return result

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5, 6]
print(get_most_even(numbers))