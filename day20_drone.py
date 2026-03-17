battery_list = []

while True:
    num = input("배터리 입력: ")

    if num == "종료":
        break
    battery_list.append(int(num))

min_battery = battery_list[0]
count = 0
total = 0

for n in battery_list:
    if n < min_battery:
        min_battery = n
    total += n

count = len(battery_list)
average = total / count

print("기록 수: ", count)
print("평균 배터리: ",average)
print("최소 배터리: ", min_battery)
