def check_battery(battery):
    if battery >= 70:
        return "충분"
    elif battery >= 30:
        return "보통"
    else:
        return "부족"
    
battery = int(input("배터리를 입력하시오: "))

result = check_battery(battery)
print(result)