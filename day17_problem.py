def get_numbers():
    numbers = []

    while True:
        num = input("숫자 입력:")

        if num == "종료":
            break

        numbers.append(int(num))
    return numbers

def calculate_sum(numbers):
    total = 0

    for n in numbers:
        total += n
    print("합:", total)

numbers = get_numbers()
calculate_sum (numbers)