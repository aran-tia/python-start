battery = 100
cmd = "전진"

battery_cost ={
    "호버" : 5,
    "전진" : 10,
    "상승" : 15
}

battery -= battery_cost[cmd]

print(battery)
