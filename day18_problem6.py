numbers = []

while True:
    num = input("숫자 입력: ")
    if num == "종료":
        break

    numbers.append(int(num))

min_num = numbers[0]
min_num1 = numbers[0]

for n in numbers:
    if n < min_num:
        min_num1 = min_num
        min_num = n
    elif n < min_num1 and n != min_num:
        min_num1 = n

print("2번쨰로 작은 값: ", min_num1)
        