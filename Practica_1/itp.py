# Práctica 1
# Carlos Hermida | Clara Lado
# Módulo Infijo a Postfijo

from stack import ArrayStack as Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] , prec["/"] = 3, 3
    prec["+"] , prec["-"] = 2, 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split(" ")

    for token in tokenList:
        if token.isalpha() or token.isnumeric():
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.is_empty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.is_empty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)