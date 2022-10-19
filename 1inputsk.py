sirka=int(input("zadaj mi sirku "))
znak=(input("zadaj zank "))

def obdlznik(sikra:int,znak:str):
    print(sirka*znak)
    print(znak + (sirka-2)*' '+znak)
    print(znak*sirka)
print(obdlznik(sirka, znak))

