commands = []

while True:
    cmd = input("명령 입력: ")


    if cmd == "종료":
        break

    
    commands.append(cmd)


for c in commands:
    print(c)


