intFirst = int(input("Enter the first integer : "))
intSecond = int(input("Enter the second integer : "))
intThird = int(input("Enter the third integer : "))

intMid = (intFirst + intSecond + intThird) / 3

great = intFirst
low = intFirst

if intSecond > intFirst :
    great = intSecond
else :
    low = intSecond
    
if intThird > great :
    great = intThird
elif intThird < low : 
    low = intThird
    

if intMid == intFirst or intMid == intSecond or intMid == intThird :    
    print("{} is the midpoint of {}, {}, {}".format(int(intMid),low,int(intMid),great))
else : 
    print("None is a midpoint of the others.")