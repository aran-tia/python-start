def get_most_even(numbers):
    count = {}

    for n in numbers:
        if n % 2 == 0:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

    max_count = 0
    max_num = 0

    for k, v in count.items():
        if v > max_count:
            max_count = v
            max_num = k

    return max_num

   

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 6, 6, 6, 6]
print(get_most_even(numbers))