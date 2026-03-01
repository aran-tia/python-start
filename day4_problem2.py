battery = int(input("배터리를 입력하시오: "))


while battery > 0:
    print("현재배터리: ", battery)
    battery = battery - 10

print("배터리 소진")

