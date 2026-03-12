text = []

while True:
    txt = input("문자 입력: ")

    if txt == "종료":
        break
    text.append(txt)

total = 0

for t in text:
    total += len(t)

print("총 문자 길이", total)
