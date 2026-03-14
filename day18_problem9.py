numbers = []

while True:
    num = input("숫자 입력: ")
    if num == "종료":
        break
    numbers.append(int(num))

max = numbers[0]
max1 = numbers[0]
max2 = numbers[0]

for n in numbers:
    if n > max:
        max2 = max1
        max1 = max
        max = n
    elif n > max1:
        max2 = max1
        max1 = n
    elif n > max2:
        max2 = n

print("1등:", max)
print("2등:", max1)
print("3등:", max2)