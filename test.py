import math

asdg = "1/6 *i **3 - 1/2 * i **2 - 1/3"
iterations = ["1", "2"]

parsed_iterations = []
for val in iterations:
    parsed_iterations.append(float(val))

until = int("50")

def parsed_Xminus(formula):
    a = formula.replace("i", iterations[0])
    return eval(a) #edit.. this wworks

#figure out how to turn string into mathematical expression
#simply create another function for iterations[1]
print(parsed_Xminus(asdg))

def test(howLong, Xminusone, Xn):
    iterations.append(Xminusone)
    iterations.append(Xn)


    # for p in range(howLong):
    #     try:
    #         iterationsvorschrift = 