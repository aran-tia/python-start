numbers = []

while True:
    num = input("숫자 입력:")
    if num == "종료":
        break
    numbers.append(int(num))

n = len(numbers)
print("입력된 숫자", n)