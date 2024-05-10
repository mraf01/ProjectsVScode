"""
Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. 
Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.
"""

def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:
    diz = {}
    for k, v in tuples:
        if k in diz:
            diz[k].append(v)
        else:
            diz[k] = [v]
    return diz

print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))
print(lista_a_dizionario([]))