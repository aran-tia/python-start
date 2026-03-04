def flight_status(battery, wind):
    if battery < 30:
        return "배터리 부족"
    elif wind > 10:
         return "강풍 위험"
    else:
        return "비행 가능"
    
battery = int(input("배터리를 입력하시오: "))
wind = int(input("풍속을 입력하시오: "))

result = flight_status(battery, wind)
print(result)