numbers = [8, 3, 15, 10, 6]

numbers.sort()

min_diff = numbers[1] - numbers[0]

for i in range(len(numbers)-1):
    diff = numbers[i+1] - numbers[i]

    if diff < min_diff:
        min_diff = diff
        a = numbers[i]
        b = numbers[i+1]

print("가장 가까운 숫자: ", a, b)