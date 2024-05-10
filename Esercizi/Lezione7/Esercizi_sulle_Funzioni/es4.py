"""
Scrivi una funzione che prenda in input una lista di dizionari che rappresentano
voti di studenti e aggrega i voti per studente in un nuovo dizionario.
"""

def aggrega_voti(voti: dict) -> dict[str:list[int]]:
    diz = {}
    for voto in voti:
        if voto['nome'] in diz:
            diz[voto['nome']].append(voto['voto'])
        else:
            diz[voto['nome']] = [voto['voto']]
    return diz

print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))
print(aggrega_voti([])) 