'''
Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione. 
L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere. 
La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.
'''

def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA or (conditionB and conditionC):
        return "Operazione permessa"
    else:
        return "Operazione negata"
    
# Test	
print(check_combination(True, False, True))  # output: Operazione permessa
print(check_combination(False, True, True))  # output: Operazione permessa
print(check_combination(False, True, False))  # output: Operazione negata
print(check_combination(True, True, True))  # output: Operazione permessa
print(check_combination(False, False, False))  # output: Operazione negata