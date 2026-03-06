commands = ["호버","전진","하강","상승"]

count = 0

for i in range(3):
    cmd = input("명령 입력: ").strip()

    if cmd in commands:
        count += 1

print("올바른 개수: ", count)
    