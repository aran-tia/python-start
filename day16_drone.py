
x = 0
y = 0
battery = 100

print("day16 자동복귀 테스트 시작")
print("시작 배터리: ", battery)
while True:
    cmd = input(":")

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
    elif cmd == "종료":
        print("프로그램 종료")
        break
    else:
        print("잘못된 명령")
        continue

    print("현재 위치:", x, y)
    print("배터리: ", battery)

    if battery <= 30:
        print("배터리 부족!")
        print("자동 복귀 시작!")
        while x != 0 or y != 0:
            if x > 0:
                x -= 1
                print("왼쪽으로 이동")
            elif x < 0:
                x += 1
                print("오른쪽으로 이동")
            elif y > 0:
                y -= 1
                print("후진 이동")
            elif y < 0:
                y += 1
                print("전진 이동")
        
            print("현재 위치: ", x, y)
        print("복귀 완료!")
        break