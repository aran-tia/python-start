def get_most_vowel(text):
    count = {}

    for n in text:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    vowel = "aeiou"
    max_count = 0
    max_vowel = ""

    for k, v in count.items():
        if k in vowel and v > max_count:
            max_count = v
            max_vowel = k
    
    return max_vowel

text = "bananaapple"
print(get_most_vowel(text))