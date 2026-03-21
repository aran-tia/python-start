class Drone:
    def __init__(self):
        self.height = 0
        self.speed = 0
        self.battery = 100
        self.commands = []

    def up(self):
        self.height += 1
        self.battery -= 5
        self.commands.append("상승")
    def down(self):
        if self.height > 0:
            self.height -= 1
            self.battery -= 5
            self.commands.append("하강")
    def accelerate(self):
        self.speed += 2
        self.battery -= 10
        self.commands.append("가속")
    def decelerate(self):
        if self.speed > 0:
            self.speed -= 1
            self.battery -= 5
            self.commands.append("감속")
    def show_status(self):
        print("현재 고도: ", self.height)
        print("현재 속도: ", self.speed)
        print("남은 배터리: ", self.battery)
        print("명령 기록: ", self.commands)

drone = Drone()

while True:
    cmd = input("명령 입력(상승/하강/가속/감속/종료): ")
    if cmd == "종료":
        break

    if cmd == "상승":
        drone.up()
    elif cmd == "하강":
        drone.down()
    elif cmd == "가속":
        drone.accelerate()
    elif cmd == "감속":
        drone.decelerate()
    else:
        continue

    drone.show_status()
    
    if drone.battery <= 0:
        print("배터리 부족! 비행 종료")
        break