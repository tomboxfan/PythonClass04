# PREPARE DATA BEGIN =============================

'''
departure time from SG: 18:40
'''

departure_hour = 18
departure_min = 40
departure_city = "Singapore"

'''
arrival time to Perth: 23:55
'''
arrival_hour = 23
arrival_min = 55
arrival_city = "Perth"

# MAIN PROGRAM BEGIN =========================

flight_hour = arrival_hour - departure_hour
flight_min = arrival_min - departure_min

print(f"The flight from {departure_city} to {arrival_city} takes {flight_hour} hour & {flight_min} minute.")