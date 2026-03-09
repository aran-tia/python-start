numbers = []

while True:
    num = input("숫자 입력: ")

    if num == "종료":
        break

    numbers.append(int(num))

total = 0

for n in numbers:
    if n % 2 == 1:
        total += n

print("홀수 합: ", total)