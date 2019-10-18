numofMonth = int(input("Enter the month (between 1 and 12 inclusive) : "))

if numofMonth < 13 and numofMonth > 0:
    if numofMonth == 1 or numofMonth == 3 or numofMonth == 5 or numofMonth == 7 or numofMonth == 8 or numofMonth == 10 or numofMonth == 12:
        print("\n\n31 days")
    elif numofMonth == 4 or numofMonth == 6 or numofMonth == 9 or numofMonth == 11:
        print("\n\n30 days")
    else:
        print("\n\n28 days")
else:
    print("Please enter valid numbers (between 1 and 12 inclusive)")