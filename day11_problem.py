battery = 100

while True:
    cmd = input("명령을 입력하시오: ")
    

    if cmd == "전진":
        battery = battery - 10
    elif cmd == "후진":
        battery = battery - 10
    elif cmd == "상승":
        battery = battery - 15
    elif cmd == "하강":
        battery = battery - 10
    elif cmd == "호버":
        battery = battery - 5
    else:
        print("잘못된 명령")
        continue


    print("남은 배터리", battery)

    if battery <= 0:
        print("비상 착륙!")
        break