import random

def get_valid_input(prompt, min_x, max_v):
    while True:
        value = int(input(prompt))
        if min_x <= value <= max_v:
            return value
        print("범위를 벗어났습니다. 다시 입력하세요")


def clamp(value, min_x, max_x):
    if value < min_x:
        return min_x
    if value > max_x:
        return max_x
    return value

def wind_warning(wind):
    if 8 <= wind <= 10:
        return "풍속 주의!"
    return ""

def battery_warning(battery):
    if 50 >= battery > 40:
        return "배터리 주의!"
    if 40 >= battery > 30:
        return "배터리 경고!"
    return ""

def apply_command(cmd, battery, wind):
    if cmd == "착륙":
        print("수동 착륙합니다.")
        return "정상 착륙", battery, wind, True
    
    elif cmd == "호버":
        print("호버중... 배터리 -5")
        battery -= 5
        wind += random.randint(-1, 2)
        return "호버", battery, wind, False
    elif cmd == "전진":
        print("전진중... 배터리 -10")
        battery -= 10
        wind += random.randint(-1, 3) 
        return "전진", battery, wind, False
    elif cmd == "상승":
        print("상승중...배터리 -15")
        battery -= 15
        wind += random.randint(0, 4)
        return "상승", battery, wind, False
    else:
        print("알 수 없는 명령입니다. (호버/전진/상승/착륙)")
        return "비행", battery, wind, False
    
def show_status(battery, wind, state):
    print("상태: ",state, "|배터리: ", battery, "|풍속:", wind)

battery = get_valid_input("배터리를 입력하시오: ", 0, 100)
wind = get_valid_input("풍속을 입력하시오: ", 0, 20)

if battery < 30 or wind > 10:
    print("비행금지")
    print("안전 대기 상태")
    state = "대기"
else:
    print("비행 가능")
    state = "비행"
    
    print("비행 시작!")
    print("시작 배터리:", battery)
    print("시작 풍속: ", wind)

    while battery > 30:
        cmd = input("명령(호버/전진/상승/착륙): ").strip()

        state, battery, wind, done = apply_command(cmd, battery, wind)

        wind = clamp(wind, 0, 20)
        if battery < 0:
            battery = 0

        print("비행중... 남은 배터리:", battery, "| 현재 풍속:", wind)
        

        msg = wind_warning(wind)
        if msg:
            print(msg)

        msg = battery_warning(battery)
        if msg:
            print(msg)
        
        if wind > 10:
            print("강풍 감지! 자동 착륙합니다")
            state = "강풍 착륙"
            break

        if done:
            break
    
    if state == "비행":
        print("배터리 부족! 자동 착륙합니다")
        state = "배터리 착륙"
print("현재 드론 상태:", state)