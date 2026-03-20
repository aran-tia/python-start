numbers = [1, 2, 3, 4, 5, 6]

def sum_even(numbers):
    total = 0

    for n in numbers:
        if n % 2 == 0:
            total += n
    
    return total

def avg_even(numbers):
    total = sum_even(numbers)
    
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
    average = total / count
    return average

total = sum_even(numbers)
average = avg_even(numbers)

print("짝수의 합:", total)
print("짝수 평균: ", average)
        