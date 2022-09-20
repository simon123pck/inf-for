x=int(input("zadaj cislo: "))
c=int(input("zadaj cislo: "))
a=int(input("zadaj cislo: "))
if x+c>a and c+a>x and a+x>c:
    print("je to trojuholik ")
    if x==c==a:
       print(" je rovnostranny")
    elif (x>a and x<c) or (x>a and x>c) or (x>c and x>a) or (c>a and a>x) or (c>a and x>a):
        print("je roynostranny")


    elif x==c:
       print("je rovnoramenny")

    elif x**2+c**2==a**2:
        print(" je pravouhly ")

else:
     print("neni to trojuholnik")