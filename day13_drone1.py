x = 0
y = 0
battery = 100
commands = []

while True:
    cmd = input("명령 입력: ")

    if cmd == "전진":
        y += 1
        battery -= 10
        commands.append(cmd)
    elif cmd == "후진":
        y -= 1
        battery -= 10
        commands.append(cmd)
    elif cmd == "오른쪽":
        x += 1
        battery -= 10
        commands.append(cmd)
    elif cmd == "왼쪽":
        x -= 1
        battery -= 10
        commands.append(cmd)
    elif cmd == "복귀":
        x = 0
        y = 0
        battery -= 10

    elif cmd == "로그":
        print("비행 기록")
        for i, c in enumerate(commands, start = 1):
            print(i, c)
        continue


    elif cmd == "종료":
        print("프로그램 종료!")
        break
    

    else:
        print("잘못된 명령!")
        continue

    if battery <= 20:
        print("배터리 부족!")
        print("자동 복귀!")
        break

    print("현재 위치:", x, y)
    print("배터리: ", battery)
