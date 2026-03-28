def longest_repeat(numbers):
    max_count = 1
    current_count = 1

    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            current_count += 1
        else:
            current_count = 1
        if current_count > max_count:
            max_count = current_count

    return max_count

numbers = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1]
print(longest_repeat(numbers))