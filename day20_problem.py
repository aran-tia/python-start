numbers = []

while True:
    num = input("숫자 입력: ")

    if num == "종료":
        break
    numbers.append(int(num))

new_list = []


for n in numbers:
    if n not in new_list:
        new_list.append(n)

for n in new_list:
    print(n)