# PREPARE DATA BEGIN =============================

departure_hour = int(input("Departure hour: "))
departure_min = int(input("Departure minute: "))
departure_city = input("Departure City: ")

arrival_hour = int(input("Arrival hour: "))
arrival_min = int(input("Arrival minute: "))
arrival_city = input("Arrival City: ")


# MAIN PROGRAM BEGIN =========================

flight_hour = arrival_hour - departure_hour
flight_min = arrival_min - departure_min

print(f"The flight from {departure_city} to {arrival_city} takes {flight_hour} hour & {flight_min} minute.")