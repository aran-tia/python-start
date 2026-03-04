commands = ["호버", "전진", "상승", "착륙"]

cmd = input("명령을 입력하시오: ")

if cmd in commands:
    print("명령 실행")
else:
    print("잘못된 명령")