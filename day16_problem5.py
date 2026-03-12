numbers = []

while True:
    num = input("숫자 입력: ")

    if num == "종료":
        break
    numbers.append(int(num))

max_num = numbers[0]

for n in numbers:
    if max_num < n:
        max_num = n
print("가장 큰 값:", max_num)