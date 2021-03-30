#!/bin/python3
nominaly = [50000, 20000,  10000, 5000, 2000, 1000, 500,  200, 100, 50,  20, 10, 5, 2, 1]
reszta = {}
wydano = []

def IleZaplacono():
    while(1):
        global zaplacono
        global zaplacono_lista
        zaplacono = 0
        print("Ile zapłacono? Proszę podać nominały oddzielone spacją (np 20 1 2)")
        zaplacono_lista = [float(x)*100 for x in input().split()]
        for x in zaplacono_lista:
            if x not in reszta:
                print("Podano nieprawidłowy nominał")
                IleZaplacono()
                return
            zaplacono = zaplacono + x
        if zaplacono>= do_zaplacenia:
            break
        else:
            print("Zapłacono za mało")


print("Wprowadź ilość nominałów do kasy")
for x in nominaly:
    print(f"{x/100}zł:")
    reszta[int(x)]=int(input())
if all(value == 0 for value in reszta.values()):
    print("Kasa jest pusta")
    print("Wprowadź ilość nominałów do kasy")
    for x in nominaly:
        print(f"{x / 100}zł:")
        reszta[int(x)] = int(input())
while(1):
    #Wyswietlanie posiadanych nominalow
    print("\n\nNominały w kasie:")
    for x in reszta.keys():
        print(f"{x/100}zł: {reszta[x]}")


    print("\nIle należy zapłacić? np 20.11")
    try:
        do_zaplacenia = float(input())*100
    except:
        print("Podano zły format kwoty")

    IleZaplacono()

    #obliczanie sumy podanych banknotów oraz reszty która musi zostać wydana
    print("Zapłacono:",zaplacono/100)
    reszta_do_wydania = zaplacono - do_zaplacenia
    reszta_do_wydania = reszta_do_wydania
    print("Reszta do wydania:", reszta_do_wydania/100)


    #dodawanie banknotów do kasy
    for x in zaplacono_lista:
            reszta[x]+=1


    #wydawanie reszty
    pomoc = {}
    pomoc = dict(reszta)
    for x in reszta.keys():
        while(1):
            if(reszta_do_wydania>=x and reszta[x]>0):
                reszta_do_wydania = reszta_do_wydania-x
                reszta[x]= reszta[x]-1
                wydano.append(x/100)
                #print("Wydano: ", x/100)
            else:
                break
    if (reszta_do_wydania==0):
        print("Wydano:")
        print(wydano)
        wydano = []
    else:
        reszta = dict(pomoc)
        print("Nie można wydać.")
        

