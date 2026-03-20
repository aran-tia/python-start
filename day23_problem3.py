numbers = [1, 8, 3, 10, 5, 2]

def even_min_max(numbers):

    max_num = None
    min_num = None

    for n in numbers:
        if n % 2 == 0:
            if max_num is None or n > max_num:
                max_num = n
            if min_num is None or n < min_num:
                min_num = n
    return max_num, min_num

max_num, min_num = even_min_max(numbers)

print("짝수 최대: ", max_num)
print("짝수 최소: ", min_num)