numbers = []

while True:
    num = input("숫자 입력: ")
    if num == "종료":
        break

    numbers.append(int(num))

print("짝수:")

for n in numbers:
    if n % 2 == 0:
        print(n)