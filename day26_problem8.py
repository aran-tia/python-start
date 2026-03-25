def get_most_letter(text):
    count = {}

    for n in text:
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

    return result[0]


text = "mississippi"
print(get_most_letter(text))