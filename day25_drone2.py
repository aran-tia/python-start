height = 0
speed = 0
battery = 100
commands = []

while True:
    cmd = input("명령 입력(상승/하강/가속/감속/종료):")
    if cmd == "종료":
        print("프로그램 종료")
        break

    commands.append(cmd)

    if cmd == "상승":
        height += 1
        battery -= 5
    elif cmd == "하강":
        if height > 0:
            height -= 1
            battery -= 5
    elif cmd == "가속":
        speed += 2
        battery -= 10
    elif cmd == "감속":
        if speed > 0:
            speed -= 1
            battery -= 5
    else:
        continue
    print("명령 기록: ", commands)

    print("현재 고도: ", height)
    print("현재 속도: ", speed)
    print("남은 배터리: ", battery)

    if battery <= 0:
        print("배터리 부족! 비행 종료")
        break