x = 0
y = 0

battery = 100

while True:
    cmd = input("명령 입력: ")

    if cmd == "전진":
        y += 1
        battery -= 10
    elif cmd == "후진":
        y -= 1
        battery -= 10
    elif cmd == "오른쪽":
        x += 1
        battery -= 10
    elif cmd == "왼쪽":
        x -= 1
        battery -= 10
    elif cmd == "복귀":
        x = 0
        y = 0
        battery -= 15
    elif cmd == "종료":
        print("프로그램 종료!")
        break
    else:
        print("잘못된 명령")
        continue
    
    print("현재 위치", x, y)
    print("배터리", battery)

    if battery < 30:
        print("비상 착륙!")
        break
