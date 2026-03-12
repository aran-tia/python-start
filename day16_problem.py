numbers = []

while True:
    num = input("숫자 입력")

    if num == "종료":
        break

    numbers.append(int(num))

min_num = numbers[0]

for n in numbers:
    if min_num > n:
        min_num = n

print("가장 작은 값: ", min_num)
