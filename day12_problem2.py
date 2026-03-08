numbers = []

while True:
    num = input("수를 입력하시오: ")

    if num == "종료":
        break

    numbers.append(int(num))

count = 0

for n in numbers:
    if n % 2 == 0:
        count += 1

print("짝수 개수: ", count)