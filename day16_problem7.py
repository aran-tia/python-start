numbers = []

while True:
    num = input("숫자 입력: ")

    if num == "종료":
        break
    numbers.append(int(num))

even_sum = 0
count = 0

for n in numbers:
    if n % 2 == 0:
        even_sum += n
        count += 1

print("짝수의 합: ", even_sum)
print("짝수 개수: ", count)