numbers = []

while True:
    num = input("고도 입력: ")

    if num == "종료":
        break
    numbers.append(int(num))

max_val = numbers[0]
min_val = numbers[0]
total = 0

for n in numbers:
    if n > max_val:
        max_val = n
    if n < min_val:
        min_val = n
    total += n

average = total / len(numbers)

print("최대 고도: ", max_val)
print("최소 고도: ", min_val)
print("평균: ", average)