name = input("이름을 입력하시오: " )
age = int(input("나이를 입력하시오: "))
battery = int(input("배터리를 입력하시오:"))

if age >= 20 or battery >=50:
    print("드론 비행 가능")
else:
    print("드론 비행 불가")


