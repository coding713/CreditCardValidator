import random

length = input("How long do you want the password? ")
if length.isdigit() and 0 < int(length) <= 30:
    pool = "abcdefghijklmnopqrstuvwxyz0123456789!@#$"
    list1 = [x for x in pool]
    passwdlen = 0
    while (passwdlen < int(length)):
        randchar = random.choice(list1)

        print(randchar, end='')
        passwdlen = passwdlen + 1
else:
    print("Please print a numerical value between 1-30")
# print()