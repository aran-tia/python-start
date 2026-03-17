fruit =  []

while True:
    cmd = input("과일 입력: ")
    if cmd == "종료":
        break
    fruit.append(cmd)

count = {}

for n in fruit:
    if n in count:
        count[n] += 1
    else:
        count[n] = 1

for n in count:
    print(n, ":", count[n])