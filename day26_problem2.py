def get_most_numbers(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    max_num = 0
    max_count = 0

    for k, v in count.items():
        if v > max_count:
            max_count = v
            max_num = k
        
    return max_num

numbers = [1, 2, 2, 3, 3, 3, 4]

result = get_most_numbers(numbers)

print("가장 많이 나온 수: ", result)