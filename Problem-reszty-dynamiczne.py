nominals = [1,2,5,10,20,50,100,200,500,1000,2000,5000,10000,20000,50000]
INFINITY = 2147483647
table= {}

payed = 0
give_it = list()
mini=INFINITY

print("Nominały w kasie:", [x/100 for x in nominals])
print("\nIle należy zapłacić?")
to_pay = float(input())*100

while 1:
    print("Ile zapłacono?")
    payed = float(input())*100

    rest = payed - to_pay
    if rest<0:
        print("zapłacono za mało")
    else:
        break

print(f"Reszta do wydania: {rest/100}")

for x in nominals:
    w = [[0]]
    table[x] = w


for x in nominals:
    for y in range(len(table[x]),int(rest+1)):
        price = y
        w = []
        while price//x!=0:
            w.append(x)
            price = price-x

        if price !=0 and nominals.index(x)==0:
            w.append(INFINITY)

        elif price !=0:
            ind = nominals[nominals.index(x)-1]
            w.extend(table[ind][price])
        table[x].append(w)

for x in table.keys():
    if len(table[x][int(rest)])<mini and INFINITY not in table[x][int(rest)]:
        mini=len(table[x][int(rest)])
        give_it = table[x][int(rest)]

if len(give_it)==0:
    print("Nie udalo sie wydac reszty")
else:
    print("Wydano:", *[f"{x/100} zł" for x in give_it])
