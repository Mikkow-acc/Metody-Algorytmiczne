import math
import operator
from sympy import *
stopien = 0
wielomian = ''
polynomial = []
wsplprzynaj = 0
wyrazwolny = 0
p = []
q = []
dziele = {}
wyndziel = {}
candidates = []
pierw = []
pierwwym = []
roots = []

def funn(a,b,q,p):
    ran = abs(int(a))
    for x in range(-ran, ran+1):
        if x==0:
            continue
        if a%x==0:
            q.append(x)

    ran = abs(int(b))
    for x in range(-ran, ran+1):
        if x==0:
            continue
        if b%x==0:
            p.append(x)

def dzielenie(a,b):
    return(int(a)/int(b))
def czywolny0(wsp,wolny,q,p,stopien,funkcja,pie,poly):
    if wolny != 0:
        funkcja(wsp, wolny, q, p)

    elif wolny == 0:
        while wolny == 0:
            if not 0 in pie:
                pie.append(0)
            stopien -= 1
            wolny = poly[stopien]
        funkcja(wsp, wolny, q, p)

print("Wprowadź stopien wielomianu")
stopien = int(input())
print("Wprowadź wspolczynnyki wielomianu (oddzielone spacją) oraz wyraz wolny")
polynomial = [int(x) for x in input().split()]
wsplprzynaj = polynomial[0]
wyrazwolny=polynomial[stopien]
print("Wielomian:")
for x in range(0,stopien+1):
    if polynomial[x] >= 0:
        poly = "+"+str(polynomial[x]) + "*"
    else:
        poly = str(polynomial[x]) + "*"
    wielomian = wielomian + poly+"x**"+str(stopien-x)
wielomian = wielomian[1:]

czywolny0(wsplprzynaj,wyrazwolny,q,p,stopien,funn,pierw,polynomial)

print(wielomian)
# print("Wspl przy najwyzszej potedze:")
# print(wsplprzynaj)
# print("Wyraz wolny:")
# print(wyrazwolny)
# print("q")
# print(q)
# print("p")
# print(p)
for x in p:
    for y in q:
        candidates.append([x,y])
#print(candidates)
for x in candidates:
    dzielenie(x[0],x[1])
    wyndziel[x[0],x[1]] = dzielenie(x[0],x[1])
for key in wyndziel:
    e = str(key[0])+"/"+str(key[1])
    dziele[e] = wyndziel[key]

# print(dziele)
# print(wyndziel)
pierwiastki = set(wyndziel.values())
# print(pierwiastki)
wynik = 0
for x in pierwiastki:
    # print("Dla wartosci " + str(x) + " wielomian " + wielomian + " ma wartosc: ")
    wynik = eval(wielomian)
    if wynik == 0:
        pierw.append(x)
    # print(wynik)
# print("pierwiastki")
# print(pierw)
for x in pierw:
    for y in wyndziel:
        if wyndziel[y] == x:
            pierwwym.append(y)
for z in pierw:
    a = 0
    pomm = wielomian
    for s in range(1,stopien):
        x = Symbol('x')
        y = eval(wielomian)
        yprime = y.diff(x)
        # print("pochodna stopnia " + str(s) + " wielomianu :")
        # print(yprime)
        # print("wartosc pochodnej dla pierwiastka: "+ str(z))
        x = z
        wynik = eval(str(yprime))
        # print(wynik)
        if wynik != 0:
            break

        wielomian = str(yprime)
        y = 0
        x = 0
        a = s
    wielomian = pomm
    pom = []
    pomoc = ""
    if z !=0:
        for key in dziele:
            if dziele[key] == z:
                pom = "("+str(key) + ")="
                pomoc += pom
    pomoc += str(z)

    print("Krotność pierwiastka " + pomoc + " to: " + str(a+1))
    pomoc = ""