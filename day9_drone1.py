commands = ["호버", "전진", "상승", "하강", "착륙"]


while True:
    battery = int(input("배터리를 입력하시오(0~100): "))

    if 0 <= battery <= 100:
        break
    else:
        print("범위를 벗어났습니다.")

while True:
    cmd = input("명령 입력: ").strip()

    if cmd == "착륙":
        print("프로그램 종료")
        break

    if cmd == "호버":
        battery -=5
    elif cmd == "전진":
        battery -=10
    elif cmd == "상승":
        battery -=15
    elif cmd == "하강":
        battery -=5


    if cmd in commands:
        print("명령 실행")
        print("현재 배터리: ", battery , "%")
    else:
        print("잘못된 명령")
        continue

    if battery <= 30:
        print("배터리 부족! 자동 착륙")
        break
