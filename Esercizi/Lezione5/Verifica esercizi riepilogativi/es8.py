""" 
Scrivi una funzione che conta e ritorna quante volte
un elemento appare isolato in una lista di numeri interi. 
Un elemento è considerato isolato se non è affiancato 
sia a destra che a sinistra da elementi uguali.
"""

def count_isolated(lista: list[int]) -> int:
    count = 0
    for i in range(len(lista)):
        if i == 0 or lista[i] != lista[i-1]: 
            if i == len(lista)-1 or lista[i] != lista[i+1]:
                count += 1
    return count

print(count_isolated([1, 2, 2, 3, 3, 3, 4]))
print(count_isolated([1, 2, 3, 4, 5]))
