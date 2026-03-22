class Drone():
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
        self.speed += 1
        self.battery -= 5
        self.commands.append("가속")
    
    def decelerate(self):
        if self.speed > 0:
            self.speed -= 1
            self.battery -= 5
            self.commands.append("감속")

    def auto_land(self):
        while self.height > 0:
            self.height -= 1
        self.commands.append("자동착륙")
    
    def check_speed(self):
        if self.speed >= 5:
            return "속도 위험"
        elif self.speed <= 1:
            return "속도 너무 느림"
        else:
            return "정상 속도"
        
    def show_status(self):
        print("현재 고도: ", self.height)
        print("현재 속도: ", self.speed)
        print("남은 배터리: ", self.battery)
        print("명령 기록: ", self.commands)
        print("상태: ", self.check_speed())
        print("-" * 20)
    
    def auto_flight(self, path):
        for cmd in path:
            if cmd == "상승":
                self.up()
            elif cmd == "하강":
                self.down()
            elif cmd == "가속":
                self.accelerate()
            elif cmd == "감속":
                self.decelerate()
            else:
                print("잘못 된 명령어")
                continue


drones = {
    "drone1" : Drone(),
    "drone2" : Drone()
}


while True:
    name = input("드론 이름 선택(drone1/drone2/종료): ")
    if name == "종료":
        break
    if name not in drones:
        print("없는 드론")
        continue

    print(name, "접속 완료")

    while True:
        cmd = input("명령 입력(상승/하강/가속/감속/상태/로그아웃):")

        if cmd == "로그아웃":
            print(name, "접속 종료")
            break

        if cmd == "상승":
            drones[name].up()
        elif cmd == "하강":
            drones[name].down()
        elif cmd == "가속":
            drones[name].accelerate()
        elif cmd == "감속":
            drones[name].decelerate()
        else:
            print("잘못된 명령어")
            continue

        drones[name].show_status()

    if drones[name].battery <= 20:
        print("배터리 부족- 자동착륙")
        drones[name].auto_land()
        drones[name].show_status()
        break

