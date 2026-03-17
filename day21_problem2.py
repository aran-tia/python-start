numbers = []

while True:
    num = input("숫자 입력:")
    if num == "종료":
        break
    numbers.append(int(num))

for n in numbers:
    if n > 3:
        print(n)