x = 0
y = 0
z = 0

while True:
    cmd = input("명령 입력: ")

    if cmd == "전진":
        y += 1
    elif cmd == "후진":
        y -= 1
    elif cmd == "왼쪽":
        x -= 1
    elif cmd == "오른쪽":
        x += 1
    elif cmd == "상승":
        z += 1
    elif cmd == "하강":
        z -= 1
    elif cmd == "종료":
        print("프로그램 종료")
        break
    else:
        print("잘못된 입력")
        continue

    print("현재 위치", x, y, z)