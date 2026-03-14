x = 0
y = 0
battery = 100

moves = {
    "전진" : (0, 1),
    "후진" : (0, -1),
    "오른쪽" : (1, 0),
    "왼쪽" : (-1, 0)
}


while True:
    cmd = input("명령 입력: ")
    
    if cmd == "종료":
        break

    if cmd in moves:
        dx, dy = moves[cmd]
        x += dx
        y += dy

        battery -= 10

        print("현재 위치: ", x, y)
        print("배터리: ", battery)    
    else:
        print("잘못된 명령")

    if battery <= 20:
        print("배터리 부족")
        print("자동 복귀 시작")

        x = 0
        y = 0
        print("복귀 완료")
        print("현재 위치: ", x, y)
        break