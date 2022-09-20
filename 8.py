x=int(input("zadaj cislo: "))
a=x%10
b=x%100
if (a+b//10)%2==0:

    print("je parny")
else:
    print("neni parny: ")