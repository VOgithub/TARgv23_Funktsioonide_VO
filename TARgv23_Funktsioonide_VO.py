from pickle import TRUE
from math import *
from random import * 
from tkinter import ROUND



print ("Hello, world!".center(50))
nimi = input ("\tMis sinu nimi on?: ").capitalize()      #str Nimi
print ("\tHello, world!"+" Tervitav sind, {0} \n". format ( nimi ))
vanus0 =int ( input ("\tMis sinu vanus on?: "))   #int vanus0
print ("\tHello, world!"+" Tervitav sind, "+ nimi +" Ma olen {0} aastat vana.\n". format ( vanus0 ))

# ulesanne 2
print("\nülesanne 2 \n")
vanus = 18    #int
eesnimi = "Jaak"  #str
kas_käib_koolis = True #bool
pikkus= 16.5  #float
print (type(vanus))
print (type(eesnimi))
print (type(pikkus))

#ülesanne 3
print("\nülesanne 3 \n")
kommmide_arv = int(input("Laual olevate kommide arv: "))
print("Laua peal on {0}". format (kommmide_arv))
mitu=int (input("Mitu kommid sa soovid süüa: "))
kommmide_arv-= mitu
print("Nüüd laual on ", kommmide_arv)

#ülesanne 4
print("\nülesanne 4 \n")
C=float(input("Ümbermõõt: \n")) #c=2*pi*r  = pi*d
d=round(C/pi,2)
print ("Läbimõõt: {0} \n". format  (d))

#ülesanne 5
print("\nülesanne 5 \n")
a=float(input("Esimene kaatet: "))
b=float(input("\nTeine kaatet: "))
d=sqrt(a**2+b**2)
print ("Diagonaal= {0} \n". format(round(hypot(a,b),3)))
print ("d = ", round(d,3))



#ülesanne 6
print("\nülesanne 6 \n")     #lovim 
try:
    aeg = float(input("\nMitu tundi kulus sõiduks? "))
    teepikkus = float(input("\nMitu kilomeetrit sõitsid? "))
    kiirus = teepikkus/aeg 
    print("Sinu kiirus oli " + str(round(kiirus)) + " km/h \n")

except :
    print ("Andmetetüüpi viga!")

#ülesanne 7
print("\nülesanne 7 \n")  
#fA=int (input("Sisesta A: "))
#fB=int (input("Sisesta B: "))
#fC=int (input("Sisesta C: "))
#fD=int (input("Sisesta D: "))
#fE=int (input("Sisesta E: "))
fA=randint(1,10)
fB=randint(1,10)
fC=randint(1,10)
fD=randint(1,10)
fE=randint(1,10)
print ("Arvude {0},{1},{2},{3},{4} Keskmine suvalisest - {5} ". format(fA,fB,fC,fD,fE,(fA+fB+fC+fD+fE)/5))




#ulesanne 8 
print("\nülesanne 8 \n")
print ("\t  @.@\n ")
print ("\t  (--)\n ")
print ("\t (\__/) \n ")
print ("\t ^^ "" ^^  \n ")



#ulesanne 9 
print("\nülesanne 9 \n")
#fA=float (input("Sisesta A in cm: "))
#fB=float (input("Sisesta B in cm: "))
#fC=float (input("Sisesta C in cm: "))
fC=randint(1,20)
fD=randint(1,50)
fE=randint(1,10)
print ("Kolmnurga ümbermõõt {0} , {1}, {2} = {3}". format (fC,fD,fE,round(fC+fD+fE,2)))


#ulesanne 10 
print("\nülesanne 10 \n")
Raha = 0.0
Kogus = int (input ("\tKui palju teil on on?: ")) # int Kogus
Raha = (((12.90 /100) *10)+12.90)/ Kogus
print ("Iga peaks maksma - {0}". format (round(Raha,2)))
