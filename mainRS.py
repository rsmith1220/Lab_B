import ADF
import postfix

print("Ingrese una expresion: ")
cadena = input()

obj = postfix.Conversion(len(cadena))

# Function call
obj.infixToPostfix(cadena)