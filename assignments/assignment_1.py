#Mailing address

name = "Parth"
street_address = "123 PG Street"
city = "Kopargaon"
state = "Maharashtra"
postal_code = "423603"
country = "India"

print(name)
print(street_address)
print(city + ", " + state + " " + postal_code)
print(country)

#########################################################################

#area of room

length=float(input("Enter length in metres: "))
width=float(input("Enter width in metres: "))
print(f"area of the room is {length*width} sq. m")

#########################################################################

#Area of a field

length=float(input("Enter length in feet: "))
width=float(input("Enter width in feet: "))
area=(length*width)/43560
print(f"Area of field is {area} acres")

#########################################################################

#Bottle deposits

small = int(input("Enter the number of small containers: "))
large = int(input("Enter the number of large containers: "))
deposit1 = 0.10
deposit2 = 0.25
refund = (small * deposit1) + (large * deposit2)
refund_text="Total refund: ${:.2f}"
print(refund_text.format(refund))

#########################################################################

#Tax and Tip

meal_cost=float(input("Enter cost of the meal: "))
tax=0.20*meal_cost
tip=0.18*meal_cost
print("Meal cost= ${:.2f}".format(meal_cost))
print("Tax= ${:.2f}".format(tax))
print("Tip= ${:.2f}".format(tip))
print("Total= ${:.2f}".format(meal_cost+tax+tip))

#########################################################################

#Height Units

print("Enter height")
feet=int(input("Enter number of feet: "))
inches=int(input("Enter inches: "))
height=(12*feet+inches)*2.54
print(f"Your height in centimeters is {height} cms")