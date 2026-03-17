numbers = []

while True:
    num = input("명령 입력: ")

    if num == "종료":
        break
    numbers.append(int(num))

count = {}

for n in numbers:
    if n in count:
        count[n] += 1
    else:
        count[n] = 1
for n in count:
    print(n, ":", count[n])