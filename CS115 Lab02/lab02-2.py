num = int(input("int : "))
while num != 0:
    
    per = 10
    count = 1
    
    while (num // per)  != 0:
        per *= 10
        count += 1
            
    per = 10**(count-1)
    num2 = 0
    
    if count % 2:
        num2 += num//(10**(count-1)) * 10**(count-1)
        num -= num//(10**(count-1)) * 10**(count-1)
        per /= 10
        for k in range(count):
            first = num // per
            num -= first*per
            per /= 10
            second = num // per
            num -= second*per
            num2 += per*first + per*second*10
            per /= 10
    else:
       for k in range(count):
            first = num // per
            num -= first*per
            per /= 10
            second = num // per
            num -= second*per
            num2 += per*first + per*second*10
            per /= 10
    print(int(num2))
    num = int(input("new int : "))