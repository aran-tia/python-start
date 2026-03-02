def check_battery_warning(battery):
    if battery <= 30:
        return "위험"
    elif battery <= 50:
        return "경고"
    else:
        return "정상"
    
battery = int(input("배터리를 입력하시오: "))

result = check_battery_warning(battery)
print(result)