def drone_status(battery, wind):
    if battery < 30 or wind > 10:
        return "비행 불가"
    elif battery <= 50:
        return "경고 비행"
    else:
        return "정상 비행"
    

battery = int(input("배터리를 입력하시오: "))
wind = int(input("풍속을 입력하시오: "))

result = drone_status(battery, wind)
print(result)
    
