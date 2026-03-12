numbers = []

while True:
    num = input("숫자 입력: ")
    if num == "종료":
        break
    numbers.append(int(num))

total = 0

print("거꾸로 출력")

for n in numbers[::-1]:
    print(n)