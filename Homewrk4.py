# Homework 3

# 3 Triangle quest

a, b, c = int(input("A=")), int(input("B=")), int(input("C="))

if a + b > c and b + c > a and c + a > b:
    print(True)
else:
    print(False)

# 2 высокосный год
# v1
import calendar
year = int(input("enter year: "))
value = calendar.isleap(year)
if value == True:
    print("year is Leap Year")
else:
    print("year isn't Leap year")

# v2
y = int(input("year: "))
if not y % 4 and y % 100 or not y % 400:
    print("Year is leap")
else:
    print("Normal year")

# 1 девятиэтажка

FLATS_IN_FLOOR = 4
FLOORS = 9
ENTRANCES = 4

flat = int(input("enter flat: "))

entrance = (flat - 1) // (FLATS_IN_FLOOR * FLOORS) + 1
floor = (flat - 1) // FLATS_IN_FLOOR - (entrance - 1) * FLOORS + 1
number_in_floor = (flat - 1) % FLATS_IN_FLOOR + 1
print((1 <= flat <= FLATS_IN_FLOOR * FLOORS * ENTRANCES) and (flat, entrance, floor, number_in_floor) or "Error")