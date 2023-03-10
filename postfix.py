class Conversion:
    
    # Constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # el array se usa para el stack
        self.array = []
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '|': 2, '?': 3}
 
    # Revisar si esta vacio el stack
    def isEmpty(self):
        return True if self.top == -1 else False
 
    # Regresar el primer valor del stack
    def peek(self):
        return self.array[-1]
 
    # Pop 
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
 
    # Push 
    def push(self, op):
        self.top += 1
        self.array.append(op)
 
   
    def isOperand(self, ch):
        return ch.isalpha()
 
    
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False
 
    # funcion de infix a postfix
    def infixToPostfix(self, exp):
        import ADF
 
        # Iterate sobre la expresion 
        for i in exp:
            
            if self.isOperand(i):
                self.output.append(i)
 
            # push si es (
            elif i == '(':
                self.push(i)
 
            
            elif i == ')':
                while((not self.isEmpty()) and
                      self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()
 
            
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)
 
        # pop 
        while not self.isEmpty():
            self.output.append(self.pop())

        
        print ("".join(self.output))
        ADF.AFD("".join(self.output))
 