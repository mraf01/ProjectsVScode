""" 
Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, 
cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.
"""

def check_parentheses(expression: str) -> bool:
    l: list = []
    for char in expression:
        if char == '(':
            l.append(char)
        elif char == ')':
            if not l or l.pop() != '(':
                return False
    return len(l) == 0

print(check_parentheses("()()"))
print(check_parentheses("(()))("))