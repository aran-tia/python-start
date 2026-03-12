numbers = []

while True:
    num = input("숫자 입력: ")

    if num == "종료":
        break
    numbers.append(int(num))

max_num = 0

for n in numbers:
    if n % 2 == 0:
        if n >  max_num:
            max_num = n
print("가장 큰 짝수", max_num)