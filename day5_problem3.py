def check_flight(battery, wind):
    if battery < 30 or wind > 10:
        return "비행금지"
    else:
        return "비행가능"

battery = int(input("배터리를 입력하시오: "))
wind = int(input("풍속을 입력하시오: "))

result = check_flight(battery, wind)
print(result)