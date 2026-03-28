def get_count_min(text):
    count = {}

    for n in text:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    min_count = 99999

    for v in count.values():
        if v >= 2 and v < min_count:
            min_count = v

    for k, v in count.items():
        if v == min_count:
            return k

text = "engineering"
print(get_count_min(text))