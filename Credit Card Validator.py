def credit_card():
    while True:
        confirm = input("Validate Credit Card? 'Yes' or 'No'? ")
        if confirm.upper() == 'YES':
            while True: 
                cnlist = input("What is your credit card number? ")

                if cnlist.isdigit() and len(cnlist) == 16:
                    cn = [int(x) for x in cnlist]
                    
                    sumx = 0
                    list_1 = cn[0::2]
                    for num in list_1:
                        x = num * 2
                        if x >= 10:
                            x = (x//10 + x%10)
                            
                        sumx = sumx + x

                    sumy = 0
                    list_2 = cn[1::2]
                    for num in list_2:
                        y = num * 1
                        sumy = sumy + y

                    sumall = sumx+sumy
                    if sumall%10 == 0:
                        print("It is valid")
                        break
                    else:
                        print("It is invalid")
                        break
                else:
                    print("Please enter a valid 16 digit credit card number!")
        else:
            break
credit_card()
