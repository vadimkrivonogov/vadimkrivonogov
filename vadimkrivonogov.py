from ast import Try
from ctypes.wintypes import INT
from math import *
from pickletools import int4
from random import *
from tkinter.tix import InputOnly



#1
print("Puu läbimõõdu arvutamine")
C=float(input("Puu ümbermõõt: "))
d=2*(C/(2*pi))
print(f"Vastus:\nPuu läbimõõduga {C} ümbermõõt võrdub {d}")

#2
print("Ristkülikukujulise maatüki diagonaal")
N=float(input("Sisesta ristküliku 1. külje pikkus => "))
M=float(input("Sisesta ristküliku 2. külje pikkus => "))
d=sqrt(N**2+M**2)
print(f"Maatüki diagonaal on {d} m**2")
 

#3

print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => "))
S=a**2
print("Ruudu pindala", round(S,1))
P=4*a
print("Ruudu ümbermõõt", round(P,1))
di=a*sqrt(2)
print("Ruudu diagonaal", round(di,2))
print()
#-----------------------------
print("Ristküliku karakteristikud")
b=float(input("Sisesta ristküliku 1. külje pikkus => "))
c=float(input("Sisesta ristküliku 2. külje pikkus => "))
S=b*c
print("Ristküliku pindala", round(S,1))
P=2*(b+c)
print("Ristküliku ümbermõõt", round(P,1))
di=sqrt(b*2+c*2)
print("Ristküliku diagonaal", round(di,1))
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => "))
d=2*r
print("Ringi läbimõõt", round(d,1))
S=pi*r**2
print("Ringi pindala", round(S,2))
C=2*pi*r
print("Ringjoone pikkus", round(C,2))


#4
try:
    A1=int(input("Sisesta 1. arv => "))    
except :
    print("Vale andmetüüp!")
    A1=0
try:
    A2=int(input("Sisesta 2. arv => "))    
except :
    print("Vale andmetüüp!")
    A2=0
try:
    A3=int(input("Sisesta 3. arv => "))    
except :
    print("Vale andmetüüp!")
    A3=0
try:
    A4=int(input("Siseta4. arv => "))
except :
    print("Vadle andmetüüp!")
    A4=0
try:
    A5=int(input("Sisesta 5. arv => "))    
except :
    print("Vale andmetüüp!")
    A5=5
Keskmine=(A1+A2+A3+A4+A5)/5
print(f"Keskmine on {Keskmine}")

#5
print("    @..@")
print("   (----)")
print("  ( \__/ )")
print("^^ "'""'" ^^ ") 

#6
a=randint(1,100)
b=randint(1,100)
c=randint(1,100)
print(f"Külg a={a}\nKülg b={b}\nKülg c={c}")
print(f"Kolmnurga ümbermõõt = {a+b+c}")
print()

#7
print("Pitsa Võtsite 3 sõbraga suure pitsa hinnaga 12,90€ te jätate teenindajale 10% jootraha")
s=10*12.90/100
s=round(s)
d=(12.90+s)
p=d/3
p=round(p,1)
print (f"Iga sõber peab maksma: {p}€")
print()

#8
print("Kütusekulu arvutamine")
l=float(input("Kasutaja sisestab tangitud kütuse liitrid: "))
km=float(input("Kasutaja sisestab läbitud kilomeetrid: "))
p=l/km*100
print (f"Vastus: {p}l/km")
print()

#9
print("Rulluisutajad")
print("Rulluisutaja keskmine kiirus on 29,9km/h")
m=24/60
t=m*29.9
t=round(t,2)
print(f"Vastus: {t}km")
print()

#10
print("Ajateisendus")
v=float(input("sisesta aja minutites: "))
t=int(v//60)
sec=int(v%60)
print(f"minutes {t}:sekundid {sec}")

#13.12.22
#1
r=randint(-100,100)
a=randint (-100,0)
print (f"{r}=)\na={a}")
if r>0 and a>0:
    Skv=a**2
    Skr=pi*r**2
    if Skv>Skr:
         print(f"Ruudu pindala {Skv} m^^2 on suurem ringi pindala {Skr} m^2")
    elif Skr>Skv:
        print(f"Ruudu pindala {Skr} m^^2 on suurem ringi pindala {Skv} m^2")
    else:
         print("Pindalad on võrised. {Skr} m^2")
else:
    print(f"(a) ja (r) paevad > kui 0 olla")
print()

#2
from math import *
from random import * 

#Määrata ja tuletada suurem kahest sisestatavast arvust.
print("Määrata ja tuletada suurem kahest sisestatavast arvust")
a=randint(-100,100)
b=randint(-100,100)
print(f"a={a}\nb={b}")
if a>b:
    print(f"arv {a} on suurem arv {b}")
elif b>a:
    print(f"arv {b} on suurem arv (a)")

print()


#Isikukoodi kontrollimine
print("Isikukoodi kontrollimine")
text=input("Palun kirjuta teie isikukod: ")
n=len(text)
if n==11 and text.isdigit(): 
    print("Teie hagikood on sisestatud õigesti")
else:
    print("iskukoodis lubamatud väärtused!")

print()


#13/12/22
r=randint(-100,100)
a=randint(-100,100)
print(f"r={r}\na={a}")
if r>0 and a>0:
    Skv=a**2
    Skr=pi*r**2
    if Skv>Skr: 
       print(f"Rudu pindala {Skv} m^2 on suurem ringi pindala {Skr} m^2")
    elif Skr>Skv:
       print(f"Rindi pindala {Skr} m^2 on suurem ruudu pindala {Skv} m^2")
    else:
       print("Pindala ov võrsed. {Skr} m^2")
else:
    print(f"{a} ja {r} peavad > kui 0 olla")
print()


print("Nädalapäevad")
try:
    p=int(input("Mis päev täna on?"))
    if   p==1:
        n="Esmaspäev"
    elif p==2:
        n="Teisipäev"
    elif p==3:
        n="Kolmapäev"
    elif p==4:
        n="Neljapäev"
    elif p==5:
        n="Reedel"
    elif p==6:
        n="Pühapäev"
    elif p==7:
        n="Laupäev"
    else:
        n="Vale Number"  
    print(n)
except:
    print("Viga")


#2
try:
    päev=int(input("Mis päev täna on?"))
except:
    print("!!!!!!")
if päev==1:
    print("Esmaspäev")
elif päev==2:
    print("Teisipäev")
elif päev==3:
    print("Kolmapäev")
elif päev==4:
    print("Neljapäev")
elif päev==5:
    print("Reedel")
elif päev==6:
    print("Pühapäev")
elif päev==7:
    print("Laupäev")
else:
    print("Viga!")


#1
try:
    hinne=int(input("Mis hinne täna said koolid"))
except:
    print("!!!!")
if hinne==5:
    print("väga hea")
elif hinne==4:
    print("Hea!")
elif hinne==3:
    print("Rahuldav")
elif hinne==2 or hinne==1: #and, or,not !=ei võrdu,<,>,>=,<=
    print("Mitte rahuldav") 
else:
    print("Viga!")

#14.12.22
try:
    vanus=int(Input("Kui vana sa oled?"))
    if vanus>18:
        print("Kas te annate vanematele loa oma Thavelit vaadata?")
        o=(input("Jah või ei."))
        if o.lower()=="jah": #upper()
             print((o))
             print("See on ligipääs teie vanematele.")
             print("Tahvel on kinni.")
        elif o.upper()=="E1":
            print("Sissepääs puudub.")
            print("Tahvel on kinni.")
    if vanus<18:
        print
   

    
 
