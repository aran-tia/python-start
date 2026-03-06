battery = 100

battery_cost = {
    "호버": 5,
    "전진": 10,
    "상승": 15
}

while True:
    cmd = input("명령을 입력하시오: ")

    if cmd == "착륙":
        print("프로그램 종료")
        break
        
    if cmd in battery_cost:
        battery -= battery_cost[cmd]
        if battery <=30:
            print("자동 착륙")
            break
        print("남은 배터리:", battery)
    else:
        print("잘못된 명령")

        




