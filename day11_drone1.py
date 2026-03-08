x = 0
y = 0 

while True:
    cmd = input("명령 입력: ").strip()

    if cmd == "전진":
        y += 1
    elif cmd == "후진":
        y -= 1
    elif cmd == "오른쪽":
        x += 1
    elif cmd == "왼쪽":
        x -= 1
    elif cmd == "복귀":
        print("자동 복귀!")
        x = 0
        y = 0
    elif cmd == "종료":
        print("프로그램 종료")
        break
    else:
        print("잘못된 명령!")
        continue
    print("현재 위치", x, y)
    