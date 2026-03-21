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

    max_speed = 0
    max_count = 0

    for k, v in count.items():
        if v > max_count:
            max_count = v
            max_speed = k
    return max_speed
        
def get_least_speed(speeds):
    count = make_count(speeds)

    min_speed = 0
    min_count = 99999

    for k, v in count.items():
        if v < min_count:
            min_count = v
            min_speed = k
    return min_speed
    
def get_second_speed(speeds):
    count = make_count(speeds)

    max_speed = 0
    max_count = 0

    max_speed1 = 0
    max_count1 = 0

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

speeds = [5, 7, 5, 9, 7, 5, 3, 3, 3, 9, 9]

most = get_most_speed(speeds)
least = get_least_speed(speeds)
second = get_second_speed(speeds)

print("가장 안정적인 속도: ", most)
print("비정상 속도: ", least)
print("보조 속도: ", second)