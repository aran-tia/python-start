numbers = [4, 4, 2, 6, 2, 4, 3]

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

print("가장 많이 나온 수: ", max_num)
    
min_count = 99999
min_num = 0

for k, v in count.items():
    if v < min_count:
        min_count = v
        min_num = k
print("가장 적게 나온 수: ", min_num)