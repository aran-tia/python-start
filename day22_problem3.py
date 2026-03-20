numbers = [1,2,3,4,5,6]

def even_info(numbers):
    count = 0
    total = 0

    for n in numbers:
        if n % 2 == 0:
            count += 1
            total += n
    return count, total

count, total = even_info(numbers)

print("짝수의 합: ", total)
print("짝수의 개수:", count)