numbers = []

while True:
    num = input("숫자 입력:")
    if num == "종료":
        break

    numbers.append(int(num))

max1 = numbers[0]
max2 = numbers[0]

for n in numbers:
    if n > max1:
        max2 = max1
        max1 = n
    elif n > max2 and n != max1:
        max2 = n

print("2번째로 큰 수", max2)