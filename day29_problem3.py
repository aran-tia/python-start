def get_unique_even(text):
    count = {}

    for n in text:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    min_count = 99999
    min_num = ""

    for k, v in count.items():
        if v <= min_count:
            min_count = v
            min_num = k

    return min_num

text = "programming"
print(get_unique_even(text))