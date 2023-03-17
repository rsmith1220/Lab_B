import postfix
# import minimizacion
from AFN_AFD import *

print("Ingrese una expresion: ")
cadena = input()

acepta = ['ε','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','*','+','|','?','(',')']

for token in cadena:
    if token not in acepta:
        print("La cadena no se acepta")
        quit()
    
    else:
        if cadena[-1]== '|' or cadena[-1]=='(' or cadena[-1]=='+' or cadena[-1]=='-':
            print("cadena no puede usarse")
            quit()
        else:
            pass
        

obj = postfix.Conversion(len(cadena))
# Function call
obj.infixToPostfix(cadena)

try:

    nfaObj = NFAfromRegex(cadena)
    nfa = nfaObj.getNFA()
    dfaObj = DFAfromNFA(nfa)
        # dfa = dfaObj.getDFA()
        # minDFA = dfaObj.getMinimisedDFA()

    nfaObj.displayNFA(0)

    dfaObj.displayDFA(1)
except:
    print("Cadena compleja")

