numbers = [10, 20, 30, 40]

def get_sum(numbers):
    total = 0

    for n in numbers:
        total += n
    
    return total

def get_avg(numbers):
    total = get_sum(numbers)
    average = total / len(numbers)
    
    return average

total = get_sum(numbers)
average = get_avg(numbers)

print("합계", total)
print("평균:",average)