n = int(input("숫자를 입력하시오: "))

total = 0

for i in range(1, n+1):
    if i % 3 == 0:
        total += i

print("3배수의 합 :", total)