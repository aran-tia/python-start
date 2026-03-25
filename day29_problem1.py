def get_multiple_letters(text):
    count = {}

    for n in text:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
    result = []

    for k, v in count.items():
        if v >= 2:
            result.append(k)
    
    return result

text = "aabbbcccde"

print(get_multiple_letters(text))