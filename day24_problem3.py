numbers = [7, 7, 7, 2, 2, 3, 3, 3, 1]

count = {}
for n in numbers:
    if n in count:
        count[n] += 1
    else:
        count[n] = 1

max_count = 0
for v in count.values():
    if v > max_count:
        max_count = v


result = []
for k, v in count.items():
    if v == max_count:
        result.append(k)
    
print("가장 많이 나온 수: ", result)
