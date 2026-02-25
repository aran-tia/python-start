battery = int(input("배터리(%): "))
wind = int(input("풍속(m/s): "))

if battery < 30:
    print("비행금지")
elif wind > 10:
    print("비행금지")
else:
    print("비행가능")