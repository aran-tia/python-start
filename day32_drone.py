def longest_up(heights):
    max_count = 1
    current_count = 1

    for i in range(1, len(heights)):
        if heights[i] > heights[i-1]:
            current_count += 1
        else:
            current_count = 1
        if current_count > max_count:
            max_count = current_count

    return max_count

heights = [10, 12, 15, 14, 16, 18, 20, 19]
print(longest_up(heights))