import ADF
import postfix

print("Ingrese una expresion: ")
cadena = input()

if cadena[-1]== '|' or cadena[-1]=='(' or cadena[-1]=='+' or cadena[-1]=='-':
    print("cadena no puede usarse")
else:
    obj = postfix.Conversion(len(cadena))

    # Function call
    obj.infixToPostfix(cadena)