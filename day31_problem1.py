def get_text_duplicate(text):
    count = {}

    for n in text:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    vowels = "aeiou"
    result = []

    for k, v in count.items():
        if v >= 2 and k in vowels:
            result.append(k)

    return result

text = "datascience"
print(get_text_duplicate(text))