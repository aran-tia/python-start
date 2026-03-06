commands = []

while True:
    cmd = input("명령을 입력하시오: ")

    if cmd == "종료":
        break

    commands.append(cmd)


print("==========비행 기록===========")

i = 1
for c in commands:
    print(i, c)
    i = i+1