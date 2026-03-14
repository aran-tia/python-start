x = 0
y = 0

moves = {
    "전진": (0, 1),
    "후진": (0, -1),
    "오른쪽": (1, 0),
    "왼쪽": (-1, 0)
}

while True:
    cmd = input("명령 입력: ")
    if cmd == "종료":
        break

    if cmd in moves:
        dx, dy = moves[cmd]
        x += dx
        y += dy
        print("현재 위치", x, y)
    else:
        print("잘못된 명령")