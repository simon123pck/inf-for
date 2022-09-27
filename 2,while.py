x=0
a=0
v=int(input("zadaj cislo: "))
while (x+v)<=100:
    a=a+1
    print(v)
    x+=v
    v=int(input("zadaj druhe cislo "))
    print("pocet je", a+1, "a scitanie je", x)
