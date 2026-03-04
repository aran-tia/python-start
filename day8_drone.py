commands = ["호버", "전진", "상승", "착륙"]

print("사용 가능한 명령: ",", ".join(commands))

cmd = input("명령 입력: ").strip()

if cmd in commands:
    print("명령 실행")
else:
    print("잘못된 명령")