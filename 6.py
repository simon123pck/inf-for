x=int(input("zadaj yacaitok"))
z=int(input("zadaj koniec:"))
c=0
for i in range(x,z):
    if i%8==0:
        c=c+1
print(c)
