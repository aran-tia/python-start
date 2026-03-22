def get_second_number(numbers):
    count = {}

    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    max_num = 0
    max_num1 = 0
    max_count = 0
    max_count1 = 0

    for k, v in count.items():
        if v > max_count:
            max_num1 = max_num
            max_count1 = max_count

            max_count = v
            max_num = k

        elif v > max_count1 and v != max_count:
            max_count1 = v
            max_num1 = k
    return max_num1


numbers = [1, 2, 2, 3, 3, 3, 4]

result = get_second_number(numbers)

print("두번째로 많이 나온 수: ", result)