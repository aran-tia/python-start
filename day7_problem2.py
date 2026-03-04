def is_safe_wind(wind):
    if wind <= 10:
        return "안전"
    else:
        return "위험"

wind = int(input("풍속을 입력하시오: "))

result = is_safe_wind(wind)
print(result)