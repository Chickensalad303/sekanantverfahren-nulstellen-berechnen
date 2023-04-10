import math

asdg = "1/6 *i **3 - 1/2 * i **2 - 1/3"
iterations = ["1", "2"]

parsed_iterations = []
for val in iterations:
    parsed_iterations.append(float(val))

until = int("50")

def parsed_Xminus(formula):
    formula_x_minusone = formula.replace("i", iterations[0])
    return eval(formula_x_minusone, {__builtins__: None}, {}) #edit.. this wworks

#figure out how to turn string into mathematical expression
#simply create another function for iterations[1]

def parsed_Xn(formula):
    formula_x_n = formula.replace("i", iterations[1])
    return eval(formula_x_n, {__builtins__: None}, {})


def test(howLong, Xminusone, Xn):
    iterations.append(Xminusone)
    iterations.append(Xn)


    # for p in range(howLong):
    #     try:
    #         iterationsvorschrift = 