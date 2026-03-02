def check_wind(wind):
    if wind > 10:
        return "비행불가"
    elif wind >= 8:
        return "주의"
    else:
        return "정상"
    
wind = int(input("풍속을 입력하시오: "))

result = check_wind(wind)
print(result)
    