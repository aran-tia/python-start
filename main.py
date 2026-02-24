n = int(input("수를 입력하시오: "))

total = 0

for i in range(1, n+1):
    if i % 3 == 0:
        total += i

print("3의 배수만 더하기:", total)