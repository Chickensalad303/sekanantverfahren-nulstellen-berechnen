import json

recv = {
    "XminusOne": "1",
    "Xn": "2",
    "formula": "1/6 *i **3 - 1/2 * i **2 - 1/3", ## error has something to do with this, everything else works
    "duration": "50",
}

# use these for the Xn & Xn-1 functions
iterations = []
iterations.append(recv["XminusOne"])
iterations.append(recv["Xn"])
print(iterations)


input_formula = recv["formula"]
duration = int(recv["duration"])


export = {}
# recieved values:
# input_formula = "1/6 *i **3 - 1/2 * i **2 - 1/3"
# iterations = ["1", "2"]
# duration = "50"

#this is not string. use this, for calculations
parsed_iterations = []
for val in iterations:
    parsed_iterations.append(float(val))



# def parsed_Xminus(formula):
#     formula_x_minusone = formula.replace("i", iterations[0])
#     return eval(formula_x_minusone, {__builtins__: None}, {}) #edit.. this wworks

# #figure out how to turn string into mathematical expression
# #simply create another function for iterations[1]

# def parsed_Xn(formula):
#     formula_x_n = formula.replace("i", iterations[1])

#     return eval(formula_x_n, {__builtins__: None}, {})


def func(p):
    a = input_formula.replace("i", str(p))
    return eval(a, {__builtins__: None}, {})

def test(howLong):
    # iterations.append(Xminusone)
    # iterations.append(Xn)


    for i in range(howLong):
        try:
            #iterationsvorschrift = parsed_iterations[1] - ( (parsed_iterations[1] - parsed_iterations[0]) / (parsed_Xn(input_formula) - parsed_Xminus(input_formula))) * parsed_Xn(input_formula)
            iterationsvorschrift = parsed_iterations[1] - ( (parsed_iterations[1] - parsed_iterations[0]) / (func(parsed_iterations[1]) - func(parsed_iterations[0])) * (func(parsed_iterations[1])) )
        except ZeroDivisionError:
            print("ein präziseres Folgenglied ist nicht zu errechnen. Die Nulstelle ist:", iterationsvorschrift)
            break

        iterations.append(str(iterationsvorschrift))
        iterations.pop(0)
        parsed_iterations.append(iterationsvorschrift)
        parsed_iterations.pop(0)

        


        i = i+1
        print("folgenglied", i, "( Xn+",i,") =", iterationsvorschrift) 

        #print("folgenglied", i, "( Xn+",i,") =", iterationsvorschrift)
        export[i] = iterationsvorschrift

    response = json.dumps(export)
    return response



test(duration)
