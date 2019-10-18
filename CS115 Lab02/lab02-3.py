a = int(input("How many rectangles : "))
count = 1
total = 0

while a:   
    wdt = int(input("Width {}:".format(count)))
    hgh = int(input("Height {}:".format(count)))
    
    for u in range(hgh):    
        for k in range(wdt):
            print('*',end='')
        print()
    a-=1
    count += 1 
    
    total += wdt*hgh
print("Total Area : {}".format(total))