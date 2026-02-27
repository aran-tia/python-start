battery = int(input("배터리를 입력하시오: "))
wind = int(input("풍속을 입력하시오: "))

if battery < 30 or wind > 10:
    print("비행 금지")
    state = "대기"
else:
    print("비행 가능")
    while battery > 30:
            battery = battery - 10
            print("비행중...남은 배터리:", battery)
    print("배터리 부족! 자동 착륙")        
    state = "이륙준비"




print("현재 드론 상태: ", state)