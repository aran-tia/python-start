n = int(input("수를 입력하시오: "))

total = 0

for i in range(1, n+1):
    if i % 2 == 0:
        total += 1

print("짝수의 개수: ", total)