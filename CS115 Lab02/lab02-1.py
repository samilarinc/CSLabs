text = input("Your message : ")
key = int(input("Encoding key : "))
num = 0
j = len(text)
tmp = ''

for i in range(len(text)):
    if ord(text[i])<123 and ord(text[i])>96: 
        num = ord(text[i])+key
        if num > 122:
            num -= 26
        elif num < 97:
            num += 26
        tmp+=chr(num)
    else:
        tmp += text[i]
        
tmp = tmp.upper()
print(tmp)