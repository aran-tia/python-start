numbers = []

while True:
    num = input("숫자 입력: ")

    if num == "종료":
        break
    numbers.append(int(num))

max_num = None

for n in numbers:
    if n % 2 == 0:
        if max_num is None or n > max_num:
            max_num = n




if max_num is None:
    print("짝수가 없습니다")
else:
    print("짝수 중 최댓값: ", max_num)
        