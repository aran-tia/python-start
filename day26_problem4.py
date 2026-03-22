def count_letters(text):
    count = {}

    for n in text:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
    return count

text = "banana"

result = count_letters(text)

print(result)
