print("This program converts feet and inches to centimeters")
feet = int(input("Enter number of feet : "))
inch = int(input("Enter number of inches : "))

totalInch = 12*feet + inch

cm = 2.54*totalInch

print("{} ft {} in = {} cm".format(feet,inch,cm))