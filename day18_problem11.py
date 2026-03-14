numbers = []

while True:
    num = input("숫자 입력: ")
    if num == "종료":
        break

    numbers.append(int(num))

numbers.sort()

n = len(numbers)

if n % 2 == 1:
    middle = numbers[n//2]
else:
    middle = (numbers[n//2 - 1] + numbers[n//2]/2)

print("중간값", middle)