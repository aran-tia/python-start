# drone_simulator_v1.py

def flight_decision(battery: int, wind: int) -> str:
    """
    비행 판단 규칙:
    - battery < 30  -> "금지"
    - wind > 10     -> "위험"
    - 그 외         -> "가능"
    """
    if battery < 30:
        return "금지"
    elif wind > 10:
        return "위험"
    else:
        return "가능"


def simulate_flight(name: str, battery: int, wind: int) -> None:
    decision = flight_decision(battery, wind)

    print("\n==============================")
    print(" 드론 자동 비행 시뮬레이터 v1")
    print("==============================")
    print(f"조종자: {name}")
    print(f"초기 배터리: {battery}% | 풍속: {wind} m/s")
    print(f"판정: {decision}")
    print("------------------------------")

    if decision == "금지":
        print("⚠️ 배터리가 너무 낮아 비행을 시작할 수 없습니다.")
        return

    # 상태 머신(아주 기초 버전)
    state = "TAKEOFF"   # TAKEOFF -> CRUISE -> LANDING -> DONE
    altitude = 0
    time_step = 0

    # 8스텝 정도만 시뮬레이션 (너무 길지 않게)
    while state != "DONE":
        time_step += 1

        # 위험 상태면 짧게만 비행하고 착륙하도록
        if decision == "위험" and time_step == 4 and state != "DONE":
            state = "LANDING"

        # 배터리 소모 (바람이 세면 더 빨리 닳는다고 가정)
        drain = 6 if wind > 10 else 4
        battery -= drain
        if battery < 0:
            battery = 0

        # 상태별 동작
        if state == "TAKEOFF":
            altitude += 10
            print(f"[{time_step:02d}] 이륙중...  고도={altitude}m | 배터리={battery}%")
            if altitude >= 20:
                state = "CRUISE"

        elif state == "CRUISE":
            print(f"[{time_step:02d}] 순항중...  고도={altitude}m | 배터리={battery}%")

            # 배터리 낮아지면 자동 착륙
            if battery < 25:
                print("⚠️ 배터리 부족 감지 → 자동 착륙으로 전환")
                state = "LANDING"

            # 적당히 순항 후 착륙
            if time_step >= 7:
                state = "LANDING"

        elif state == "LANDING":
            altitude -= 10
            if altitude < 0:
                altitude = 0
            print(f"[{time_step:02d}] 착륙중...  고도={altitude}m | 배터리={battery}%")
            if altitude == 0:
                state = "DONE"

        # 완전 방전이면 즉시 종료
        if battery == 0 and state != "DONE":
            print("🛑 배터리 0% → 비상 착륙!")
            state = "DONE"

    print("------------------------------")
    print("✅ 비행 종료. 기록이 저장되었습니다(가정).")
    print("==============================\n")


def main():
    name = input("이름: ")
    battery = int(input("배터리(%): "))
    wind = int(input("풍속(m/s): "))

    simulate_flight(name, battery, wind)


if __name__ == "__main__":
    main()