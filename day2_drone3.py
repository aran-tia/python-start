battery = int(input("배터리를 입력하시오: "))
wind = int(input("풍속을 입력하시오: "))

if battery >= 70 and wind < 5:
    print("안전 비행")
elif battery >= 40:
    print("주의 비행")
else:
    print("비행 금지")