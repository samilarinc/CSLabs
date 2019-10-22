def square_digits(number):
    """
    This function takes positive integers as input and returns an integer
    in which every digit of the input is squared int he same order.
    """
    numStr = str(number)
    newStr = ''
    
    for i in numStr:
        j = int(i)
        j **= 2
        newStr += str(j)

    return int(newStr)

num = int(input("Enter an int : "))
while num != -1:
    num = square_digits(num)
    print("number with squared digits is " + str(num))
    num = int(input("Enter an int : "))
print("bye")
