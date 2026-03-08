numbers = []

while True:
    num = input("숫자를 입력하시오: ")
    
    if num == "종료":
        break

    numbers.append(int(num))


min_num = numbers[0]
max_num = numbers[0]

for n in numbers:
    if n < min_num:
        min_num = n
    if n > max_num:
        max_num = n

print("최대값", max_num)
print("최솟값", min_num)