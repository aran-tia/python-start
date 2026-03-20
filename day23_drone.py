commands = []


while True:
    cmd = input("명령 입력:")
    if cmd == "종료":
        break
    commands.append(cmd)

    def count_commands(commands):
        count = {}
        for cmd in commands:
            if cmd in count:
                count[cmd] += 1
            else:
                count[cmd] = 1
        return count

    def get_max_commands(count_dict):
        max_cmd = ""
        max_count = 0

        for k, v in count_dict.items():
            if v > max_count:
                max_count = v
                max_cmd = k
        return max_cmd
    
count_dict = count_commands(commands)

for k, v in count_dict.items():
    print(k, ":", v)

max_cmd = get_max_commands(count_dict)
print("가장 많이 사용된 명령: ", max_cmd)



