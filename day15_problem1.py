word = []

while True:
    wd = input(":")
    if wd == "종료":
        break

    word.append(wd)

max_len = 0

for i in word:
    if len(i) > max_len:
        max_len = len(i)

print("가장 긴 길이: ", max_len)