def longest_decrease(numbers):
    max_count = 1
    current_count = 1

    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            current_count += 1
        else:
            current_count = 1

        if current_count > max_count:
            max_count = current_count

    return max_count

numbers = [9, 7, 5, 6, 4, 3, 2, 8]
print(longest_decrease(numbers))