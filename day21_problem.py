numbers = []

while True:
    num = input("숫자 입력: ")

    if num == "종료":
        break
    numbers.append(int(num))

count = 0
sum = 0

for n in numbers:
    if n % 2 == 0:
        count += 1
        sum += n
print("짝수 개수: ", count)
print("짝수의 합:" , sum)