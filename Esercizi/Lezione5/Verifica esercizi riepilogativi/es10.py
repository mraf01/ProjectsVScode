"""
Scrivi una funzione che unisce due dizionari. 
Se una chiave è presente in entrambi, somma i loro valori.
"""

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    diz = dict1
    for key, value in dict2.items():
        if key in diz:
            diz[key] += value
        else:
            diz[key] = value
    return diz

print(merge_dictionaries({'x': 5}, {'x': -5}))