numbers = [1, 2, 1, 3, 2, 1]

count = {}

for n in numbers:
    if n in count:
        count[n] += 1
    else:
        count[n] = 1

max_num = 0
max_count = 0

for k, v in count.items():
    if v > max_count:
        max_count = v
        max_num = k

print("가장 많이 나온 숫자: ", max_num)

min_num = None
min_count = None

for k, v in count.items():
    if min_count is None or v < min_num:
        min_num = v
        min_count = k

print("가장 적게 나온 수: ", min_num)