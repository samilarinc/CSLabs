import random

def throwUntil(n, summ):
    dice = 0
    counter = 0
    while dice != summ:
        dice = 0
        counter += 1
        for i in range(n):
            a = random.randint(1,6)
            print(a, end=' ')
            dice += a
        print()
    return counter

n = int(input("Enter number of dice: "))
summ = int(input("Enter desired sum of dice: "))
while summ > 6*n or summ < n:
    print("Invalid sum for the specified number of dice\n")
    summ = int(input("Enter desired sum of dice: "))

counter = throwUntil(n, summ)

print("{} dice are rolled {} times to get desired sum {}".format(n, counter, summ))


                    
