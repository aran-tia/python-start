import random

while True:
    battery = int(input("배터리를 입력하시오: "))
    if 0 <= battery <= 100:
        break
    print("범위를 벗어났습니다. 다시 입력하세요.")
while True:    
    wind = int(input("풍속을 입력하시오: "))
    if 0 <= wind <= 20:
        break
    print("범위를 벗어났습니다. 다시 입력하세요")

if battery < 30 or wind > 10:
    print("비행금지")
    print("안전 대기 상태")
    state = "대기"
else:
    print("비행 가능")
    state = "비행"
    
    print("비행 시작!")
    print("시작 배터리: ", battery)
    print("시작 풍속", wind)

    while battery > 30:
        cmd = input("명령(호버/전진/상승/착륙): ").strip()

        if cmd == "착륙":
            print("수동 착륙합니다.")
            state = "정상 착륙"
            break
        elif cmd == "호버":
            state = "호버"
            battery -= 5
            wind += random.randint(-1, 2)
            print("호버 중... 배터리 -5")
        elif cmd =="전진":
            state = "전진"
            battery -= 10
            wind += random.randint(-1, 3)
            print("전진 중... 배터리 -10")
        elif cmd == "상승":
            state = "상승"
            battery -= 15
            wind += random.randint(0, 4)
            print("상승 중... 배터리 -15")
        else:
            print("알 수 없는 명령입니다. (호버/전진/착륙)")
            continue

        if wind < 0:
            wind = 0
        if wind >20:
            wind = 20
        print("비행중... 남은 배터리:", battery, "| 현재 풍속: ", wind)

        if wind >= 8 and wind <= 10:
            print("풍속 주의 !")
        if battery <= 50 and battery > 40:
            print("배터리 주의!")
        if battery <= 40 and battery > 30:
            print("배터리 경고!")


        if wind > 10:
            print("강풍 감지! 자동 착륙합니다.")
            state = "강풍 착륙"
            break

    if state == "비행":
        print("배터리 부족! 자동 착륙합니다.")
        state = "배터리 착륙!"

    
print("현재 드론 상태: ", state)                 