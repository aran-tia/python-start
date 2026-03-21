numbers = [1,2,2,3,3,3,4,4,4,4]

max1 = 0
max1_num = 0

max2 = 0
max2_num = 0

count = {}
for n in numbers:
    if n in count:
        count[n] += 1
    else:
        count[n] = 1



for k, v in count.items():
    if v > max1:
        max2 = max1
        max2_num = max1_num

        max1 = v
        max1_num = k
    elif v > max2:
        max2 = v
        max2_num = k
    


print("두번째로 가장 많이 나온 수: ", max2_num)