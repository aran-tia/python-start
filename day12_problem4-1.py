numbers = []

while True:
    num = input("숫자 입력:")

    if num == "종료":
        break

    numbers.append(int(num))

total = 0
max_num = numbers[0]
min_num = numbers[0]

for n in numbers:
    total += n

average = total / len(numbers)

for n in numbers:
    if n > max_num:
        max_num = n
    if n < min_num:
        min_num = n

print("합: ", total)
print("평균: ", average)
print("최대값: ", max_num)
print("최솟값: ", min_num)