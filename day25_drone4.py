class Drone:
    def __init__(self):
        self.height = 0
        self.speed = 0
        self.battery = 100
commands = []
while True:
    cmd = input("명령 입력(상승/하강/가속/감속/종료):")
    if cmd == "종료":
        break

    commands.append(cmd)

    def up(self):
        height += 1
        battery -= 5
    
    def down(self):
        if height > 0:
            height -= 1
            battery -= 5

    def accelerate(self):
        speed += 2
        battery -= 10

    def decelerate(self):
        if speed > 0:
            speed -= 1
            battery -= 5

    def show_status(self):
        print("현재 고도: ", up(self))
        print("현재 속도: ", down(self))
        print("남은 배터리: ", accelerate(self))
        print("명령 기록: ", decelerate(self))
