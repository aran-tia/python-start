heights = [10, 12, 10, 15, 12, 10, 8, 8, 8, 15]

count = {}
for n in heights:
    if n in count:
        count[n] += 1
    else:
        count[n] = 1

max_count = 0
max_num = 0
min_count = 99999
min_num = 0

for k, v in count.items():
    if v > max_count:
        max_count = v
        max_num = k

print("가장 많이 나온 고도: ", max_num)

for k, v in count.items():
    if v < min_count:
        min_count = v
        min_num = k

print("가장 적게 나온 고도: ", min_num)

if max_num >= 15:
    print("고도 높음-위험")
else:
    print("안전 비행")