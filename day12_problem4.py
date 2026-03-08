numbers = []

while True:
    num = input("숫자 입력: ")

    if num == "종료":
        break

    numbers.append(int(num))

min_num = numbers[0]
max_num = numbers[0]

total = 0

for n in numbers:
    total += n

average = total / len(numbers)
print("평균", average)

for n in numbers:
    if n > max_num:
        max_num = n
    if n < min_num:
        min_num = n

print("최대값: ",max_num)
print("최솟값: ",min_num)

print("합", total)