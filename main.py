import json
from sympy.parsing.sympy_parser import parse_expr



results = []


l = []

export = {
    "error": 0,
}

# recv = {
#     "XminusOne": "1",
#     "Xn": "2",
#     "formula": "1/6 *i **3 - 1/2 * i **2 - 1/3",
#     "duration": "50",
# }




# try:
#     howLong = int(input("bis welches folgenglied?: "))
# except ValueError:
#     print("bitte eine positive, ganze zahl eingeben")
#     quit()

# Xnminusone = float(input("enter the first number Xn-1:"))
# Xn = float(input("enter the second number Xn:"))
# l.append(Xnminusone)
# l.append(Xn)



# good writeup on eval():  https://www.programiz.com/python-programming/methods/built-in/eval
def func(i, formula): ##this param gets accessed by eval/parse_expr statement    
    #https://docs.sympy.org/latest/modules/parsing.html
    return parse_expr(formula, {"i":i}, {}) # apparently eval() isn't safe. tho this is an alternative but i have no idea if this one is safe
    #return eval("1/6 *i **3 - 1/2 * i **2 - 1/3", {__builtins__:None}, {"i":i})

 
def calculate(Xnminusone, Xn, formula, howLong):
    # howLong = int(recv["duration"])

    # Xnminusone = float(recv["XminusOne"])
    # Xn = float(recv["Xn"])
    results.clear()
    l.clear()
    l.append(Xnminusone)
    l.append(Xn)

    for p in range(howLong):

        # iterationsvorschrift = Xn - (   (Xn - Xnminusone) / (func(Xn) - func(Xnminusone)) * (func(Xn))   )
        try:
            iterationsvorschrift = l[1] - (   (l[1] - l[0]) / (func(l[1], formula) - func(l[0], formula)) * (func(l[1], formula))   )
        except ZeroDivisionError:
            print("ein präziseres Folgenglied ist nicht zu errechnen. Die Nulstelle ist:", iterationsvorschrift)
            export["error"] = 2
            export["message"]  ="ein präziseres Folgenglied ist nicht zu errechnen. Die Nulstelle ist:"
            export["errType"] = "ZeroDivisionError"
            export["current_value"] = iterationsvorschrift
            break
            
        l.append(iterationsvorschrift)
        
        l.pop(0)
        p = p+1
        
        print("folgenglied", p, "( Xn+",p,") =", iterationsvorschrift) 

        results.append(iterationsvorschrift)
    
    results.pop(len(results) - 1)
    export["result"] = results

    
    response = json.dumps(export)
    return response






