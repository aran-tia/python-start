def get_text_duplicate(text):
    count = {}

    for n in text:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    max_count = 0
    max_char = " "

    for k, v in count.items():
        if v > max_count:
            max_count = v
            max_char = k
        
    return max_char

text = "hello world"
print(get_text_duplicate(text))