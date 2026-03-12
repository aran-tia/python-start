numbers = []

while True:
    num = input("숫자 입력:")
    if num == "종료":
        break
    numbers.append(int(num))

total = 0

for n in numbers:
    total += n
    average = total / len(numbers)

print("평균:", average)