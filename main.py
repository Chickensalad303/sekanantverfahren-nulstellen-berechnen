l = []
howLong = int(input("bis welches folgenglied?: "))

Xnminusone = int(input("enter the first number Xn-1:"))
Xn = int(input("enter the second number Xn:"))
l.append(Xnminusone)
l.append(Xn)

def func(i):
    return 1/6 *i **3 - 1/2 * i **2 - 1/3

for p in range(howLong):
    # iterationsvorschrift = Xn - (   (Xn - Xnminusone) / (func(Xn) - func(Xnminusone)) * (func(Xn))   )
    try:
        iterationsvorschrift = l[1] - (   (l[1] - l[0]) / (func(l[1]) - func(l[0])) * (func(l[1]))   )
    except ZeroDivisionError:
        print("ein präziseres Folgenglied ist nicht zu errechnen. Die Nulstelle ist:", iterationsvorschrift)
        break
    l.append(iterationsvorschrift)
    l.pop(0)
    p = p+1
    print("folgenglied", p, "( Xn+",p,") =", iterationsvorschrift) 