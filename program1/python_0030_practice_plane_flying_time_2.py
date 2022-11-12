# PREPARE DATA BEGIN =============================

'''
departure time from SG: 10:01
'''

departure_hour = 10
departure_min = 1
departure_city = "Singapore"

'''
arrival time to Kuala Lumpor: 11:05
'''
arrival_hour = 11
arrival_min = 5
arrival_city = "Kuala Lumpor"




# MAIN PROGRAM BEGIN =========================

flight_hour = arrival_hour - departure_hour
flight_min = arrival_min - departure_min

print(f"The flight from {departure_city} to {arrival_city} takes {flight_hour} hour & {flight_min} minute.")