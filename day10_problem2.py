battery = 100

while True:
    print(f"현재 배터리: {battery}%")
    if battery <= 30:
        print("자동 착륙")
        break
    battery -= 10