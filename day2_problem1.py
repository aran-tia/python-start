n = int(input("수를 입력하시외: "))

total = 0 

for i in range(1, n+1):
    if i % 5 == 0:
        total += i

print("5의 배수의 합: ", total)