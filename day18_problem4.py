numbers = []

while True:
    num = input("숫자 입력: ")
    if num == "종료":
        break
    
    numbers.append(int(num))

total = 0
max_num = numbers[0]
min_num = numbers[0]
count = 0

for n in numbers:
    total += n

    if n > max_num:
        max_num = n
    
    if n < min_num:
        min_num = n

    if n % 2 == 0:
        count += 1
        
average = total / len(numbers)

print("총합: ", total)
print("평균: ", average)
print("최댓값: ", max_num)
print("최솟값: ", min_num)
print("짝수 개수: ", count)