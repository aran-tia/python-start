numbers = []

while True:
    num = input("숫자 입력:")

    if num == "종료":
        break

    numbers.append(int(num))

max_num = numbers[0]
max_num1 = numbers[0]
max_num2 = numbers[0]

for n in numbers:
    if n > max_num:
        max_num2 = max_num1
        max_num1 = max_num
        max_num = n
    elif n > max_num1:
        max_num2 = max_num1
        max_num1 = n
    elif n > max_num2:
        max_num2 = n


print("1등: ",max_num)
print("2등: ",max_num1)
print("3등: ",max_num2)