words = []

while True:
    wd = input("단어 입력: ")

    if wd == "종료":
        break
    words.append(wd)

max_word = ""
max_len = 0

for n in words:
    if len(n) > max_len:
        max_len = len(n)
        max_word = n
 
    
print("가장 긴 단어: ", max_word)
print("길이: ", max_len)