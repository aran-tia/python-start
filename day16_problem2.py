distance = 0

while True:
    cmd = input("명령 입력:")
    
    if cmd == "종료":
        break

    if cmd == "전진":
        distance += 1
    elif cmd == "후진":
        distance += 1
    elif cmd == "왼쪽":
        distance += 1
    elif cmd == "오른쪽":
        distance += 1
    else:
        continue

print("이동한 거리:", distance)