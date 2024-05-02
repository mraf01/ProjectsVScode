"""
Scrivi una funzione che rimuove tutti i duplicati da una lista, 
contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.
"""

def remove_duplicates(lista: list[int | str]) -> list[int | str]:
    l = []
    for elemento in lista:
        if elemento not in l:
            l.append(elemento)
    return l

print(remove_duplicates([1, 2, 3, 1, 2, 4]))