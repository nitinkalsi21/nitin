print("1-Addition\n2-Substraction\n3-Division\n4-Multiplication\n5-Power to\n6-Rounding\n7-Remaining\n00-Exit")
Nit = True
while Nit is True:
    First = int(input("Enter First Number:"))
    if First == 00:
        print("closing the app")
        exit()
    Second = int(input("Enter Second Number:"))
    if Second == 00:
        print("closing the app")
        exit()
    Opretor = int(input("Enter The Opretor:"))
    if Opretor==1:
        Sum = First+Second
        print(Sum)
    elif Opretor==2:
        Sum = First- Second
        print(Sum)
    elif Opretor==3:
        Sum = First/Second
        print(Sum)
    elif Opretor==4:
        Sum = First*Second
        print(Sum)
    elif Opretor==5:
        Sum = First**Second
        print(Sum)
    elif Opretor==6:
        Sum = First//Second
        print(Sum)
    elif Opretor==7:
        Sum = First%Second
        print(Sum)
    elif Opretor==00:
        print("closing the app")
        Nit = False
    else:
        print("Wrong Input Try again")


