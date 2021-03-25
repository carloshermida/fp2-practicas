# Práctica 1
# Carlos Hermida | Clara Lado
# Módulo Cálculos
from writingcheck import check_spaces, check_brackets
from itp import infixToPostfix
from stack import ArrayStack as Stack

def operador(op, num1, num2):
    if op == "+":
        resultado = num1 + num2
        return resultado
    
    elif op == "-":
        resultado = num1 - num2
        return resultado 
    
    elif op == "*":
        resultado = num1 * num2
        return resultado 
    
    elif op == "/":
        resultado = num1/num2
        return resultado
    
    elif op == "**":
        resultado = num1**num2
        return resultado 
    
    else:
        return "Operando no válido"

def iniciar(): 
    infijo = input("Introduce una expresion infija: ")
    
    if check_spaces(infijo) and check_brackets(infijo):
        postfijo = infixToPostfix(infijo)
        lista_postfijo = postfijo.split(" ")
        simbolos = ["+", "-", "*", "/", "**"]
        pila = Stack()
    
        for item in lista_postfijo:
            pila.push(item)
            if item in simbolos:
                op = pila.pop()
                num2 = int(pila.pop())
                num1 = int(pila.pop())
                pila.push(int(operador(op, num1, num2)))
    
        print(pila.peek())
    
    print("Algo anda mal amigo")