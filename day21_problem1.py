numbers = []

while True:
    num = input("숫자 입력: ")

    if num == "종료":
        break
    numbers.append(int(num))

min_num = numbers[0]

for n in numbers:
    if n < min_num:
        min_num = n

print("최소값 찾기: ", min_num)