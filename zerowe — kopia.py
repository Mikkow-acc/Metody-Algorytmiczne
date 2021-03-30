import math
polynomial = [0,2,-6,4]
numerator_candidates = []
denominator_candidates = []
candidates = []
roots = []


def HornerScheme(z,y):
    global polynomial
    new_poly = []
    new_poly.append(polynomial[-1])
    for x in range(len(polynomial)-2,-1,-1):
        if new_poly[-1]!=0:
            value = (new_poly[-1]*z/y)+polynomial[x]
            new_poly.append(value)
        else:
            new_poly.append(polynomial[x])

    if new_poly[-1] == 0:
        del new_poly[-1]
        new_poly.reverse()
        polynomial = new_poly.copy()
        roots.append([z,y])

numerator_candidates.append(polynomial[0])
denominator_candidates.append(polynomial[-1])

i=0

for x in range(len(polynomial)):
    if polynomial[x]>0:
        i=x
        break

ran = abs(polynomial[x])
for x in range(-ran, ran):
    if x==0:
        continue
    if polynomial[0]%x==0:
        numerator_candidates.append(x)

ran = abs(int(polynomial[-1]/2)+1)
for x in range(-ran, ran):
    if x==0:
        continue
    if polynomial[-1]%x==0:
        denominator_candidates.append(x)


for x in denominator_candidates:
    for y in numerator_candidates:
        if x!=0:
            HornerScheme(y,x)

roots_d=[]
roots_copy = roots.copy()
#Wyswietlanie
for x in range(len(roots)-1,-1,-1):
    if roots[x][1]==1:
        roots_d.append(roots[x][0])
        del roots_copy[x]
    elif roots[x][1] == -1:
        roots_d.append(-roots[x][0])
        del roots_copy[x]
    elif roots[x][0] == 0:
        roots_d.append(0)
        del roots_copy[x]
    elif roots[x][0] == roots[x][1]:
        roots_d.append(1)
        del roots_copy[x]

print("Roots: ", *roots_d, end=" ")
print(*[f"{x[0]}/{x[1]} " for x in roots_copy])
