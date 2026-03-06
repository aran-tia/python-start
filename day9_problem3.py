commands = ["호버", "전진", "상승", "하강", "착륙"]


while True:
    battery = int(input("배터리를 입력하시오(0~100): "))

    if 0 <= battery <= 100:
        break
    else:
        print("범위를 벗어났습니다.")

battery_cost = {
        "호버" : 5,
        "전진" : 10,
        "상승" : 15,
        "하강" : 5
    }

while True:
    cmd = input("명령 입력: ").strip()

    if cmd == "착륙":
        print("프로그램 종료")
        break

    
    if cmd not in battery_cost:
        print("잘못된 명령")
        continue
    battery -= battery_cost[cmd]


    if cmd in commands:
        print("명령 실행")
        print(f"현재 배터리: {battery}%")
    else:
        print("잘못된 명령")
        continue

    if battery <= 30:
        print("배터리 부족! 자동 착륙")
        break
