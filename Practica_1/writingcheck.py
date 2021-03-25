# Práctica 1
# Carlos Hermida | Clara Lado
# Módulo Comprobación de escritura

def check_spaces(infijo):
    total = len(infijo)
    caracteres = len(infijo.split())
    if total - caracteres == caracteres - 1:
        return True
    else:
        return False
    
def check_brackets(infijo):
    infijo = infijo.split()
    if infijo.count("(") ==infijo.count(")"):
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
    simbolos = ["+", "-", "*", "/", "**"]
    infijo = infijo.split()
    if infijo[0] or infijo[-1] in simbolos:
        return False
    else:
        for simbolo in simbolos:
            