def get_valid_input(prompt, min_v, max_v):
    while True:
        value = int(input(prompt))

        if min_v <= value <= max_v:
            return value
        
        print("범위를 벗어났습니다.")

        
battery= get_valid_input("배터리를 입력하시오:", 0, 100)
wind = get_valid_input("풍속을 입력하시오: ", 0, 20)

print("배터리:", battery)
print("풍속: ", wind)