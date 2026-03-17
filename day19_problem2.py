words = []

while True:
    cmd = input("문자 입력:")
    if cmd == "종료":
        break
    
    words.append(cmd)

count = {}

for n in words:
    if n in count:
        count[n] += 1
    else:
        count[n] = 1

max_words = ""
max_count = 0

for k, v in count.items():
    if v > max_count:
        max_count = v
        max_words = k




print("가장 많이 나온 단어: ", max_words)
print("횟수: ", max_count)