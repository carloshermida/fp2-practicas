# Práctica 1
# Carlos Hermida | Clara Lado
# Módulo Comprobación de escritura
from itp import infixToPostfix
from stack import ArrayStack as Stack

def check_spaces(infijo):
    """ Funci�n que comprueba la presencia de todos los especios necesarios para separar los caracteres  """
    total = len(infijo)
    caracteres = len(infijo.split())
    if total - caracteres == caracteres - 1:
        return True
    else:
        return False
    
def check_brackets(infijo):
    """ Funci�n que comprueba la correcta posici�n de los par�ntesis y que no falte ninguno """
    infijo = infijo.split()
    if infijo.count("(") == infijo.count(")"):
        if infijo.count("[") == infijo.count("]"):
            i = 0
            while i <= len(infijo):
                if infijo.index("(") < infijo.index(")"):
                    infijo.remove("(")
                    infijo.remove(")")
                else:
                    return False
                i += 1
            return True
       
    return False

def proximity_symbols(infijo):
    """ Funci�n que revisa que los signos matem�ticos esten bien puestos """
    simbolos = ["+", "-", "*", "/", "**"]
    infijo = infijo.split()
    if infijo[0] or infijo[-1] in simbolos:
        return False
    else:
        for simbolo in simbolos:
            postfijo = infixToPostfix(infijo)
            lista_postfijo = postfijo.split(" ")
            simbolos = ["+", "-", "*", "/", "**"]
            pila = Stack()
            a = 0
            b = 0
            for item in lista_postfijo:
                
                if item in simbolos:
                    b = a
                    a = item
                    if a == b:
                        return False
            return True
                   
        
 #igual son burradas que se podrian hacer mucho mas simples, por cierto, este error de abjo si lo metemos el la funcion
#encagrada de operar era muy sencillo, tmb podriamos poner en la f iniciar antes de pila peak un if que si op==/ y num2==0 haga        
def correct_division(infijo):
     """ Funci�n encargada de """
        postfijo = infixToPostfix(infijo)
        lista_postfijo = postfijo.split(" ")
        
        pila = Stack()
    
        for item in lista_postfijo:
            pila.push(item)
            if item == 0:
                cero = int(pila.pop())
                elemento = pila.pop()
                if elemento == "/":
                    return False
            return True