numbers = []

while True:
    num = input("숫자 입력: ")

    if num == "종료":
        break
    numbers.append(int(num))

min1 = numbers[0]
min2 = numbers[0]
min3 = numbers[0]

for n in numbers:
    if n < min1:
        min3 = min2
        min2 = min1
        min1 = n

    elif n < min2:
        min3 = min2
        min2 = n
    
    elif n < min3:
        min3 = n

print("가장 작은값: ")
print(min1)
print(min2)
print(min3)