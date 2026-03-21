def make_count(speeds):
    count = {}

    for n in speeds:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    return count

def get_most_speed(speeds):
    count = make_count(speeds)

    max_count = 0
    max_speed = 0

    for k, v in count.items():
        if v > max_count:
            max_count = v
            max_speed = k
    return max_speed

def get_least_speed(speeds):
    count = make_count(speeds)

    min_count = 99999
    min_speed = 0

    for k, v in count.items():
        if v < min_count:
            min_count = v
            min_speed = k
    return min_speed 

def get_second_speed(speeds):
    count = make_count(speeds)

    max_count = 0
    max_count1 = 0
    max_speed = 0
    max_speed1 = 0

    for k, v in count.items():
        if v > max_count:
            max_count1 = max_count
            max_speed1 = max_speed

            max_count = v
            max_speed = k
        elif v > max_count1:
            max_count1 = v
            max_speed1 = k
    return max_speed1

def get_average_speed(speeds):
    total = 0

    for n in speeds:
        total += n
    
    average = total / len(speeds)
    return average

def get_danger_speeds(speeds):
    result = []

    for n in speeds:
        if n >= 10:
            result.append(n)
    return result

speeds =[5, 7, 5, 9, 7, 5, 3, 3, 3, 9, 9, 12, 1]

most = get_most_speed(speeds)
least = get_least_speed(speeds)
second = get_second_speed(speeds)
avg = get_average_speed(speeds)
danger = get_dangers_speeds(speeds)

print("가장 안정적인 속도:", most)
print("비정상 속도:", least)
print("보조 속도: ", second)
print("평균 속도: ", avg)
print("위험 속도 목록: ", danger)



