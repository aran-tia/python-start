def battery_percent(battery):
    if battery >= 80:
        return "높음"
    elif battery >= 40:
        return "보통"
    else:
        return "낮음"
    
battery = int(input("배터리를 입력하시오: "))

result = battery_percent(battery)
print(result)