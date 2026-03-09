import random
x = 0
y = 0
battery = 100

treasure_x = random.randint(0,4)
treasure_y = random.randint(0,4)

while True:
    num = input("명령 입력: ")
    
    if num == "전진":
        y += 1
        battery -= 10
    elif num == "후진":
        y -= 1
        battery -= 10
    elif num == "오른쪽":
        x += 1
        battery -= 10
    elif num == "왼쪽":
        x -= 1
        battery -= 10 
    elif num == "종료":
        print("게임 종료")
        break
    else:
        print("다시 입력하시오")
        continue
    if x < 0 or x > 4 or y < 0 or y > 4:
            print("맵 밖으로 나갈 수 없습니다!")
            x = max(0, min(x,4))
            y = max(0, min(y,4))
    if battery == 0:
        break
    print("현재 위치: ", x, y)
    print("배터리:", battery)

    if x == treasure_x and y == treasure_y:
        print("보물 발견!")
        break
    if x < treasure_x:
        print("보물이 동쪽에 있습니다")
    elif x > treasure_x:
        print("보물이 서쪽에 있습니다")
    if y < treasure_y:
        print("보물이 북쪽에 있습니다")
    elif y > treasure_y:
        print("보물이 남쪽에 있습니다")
print("보물 위치: ", treasure_x, treasure_y)