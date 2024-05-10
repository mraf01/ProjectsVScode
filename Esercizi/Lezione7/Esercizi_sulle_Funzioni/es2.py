"""
Scrivi una funzione che, data una lista, ritorni un dictionary che mappa 
ogni elemento alla sua frequenza nella lista.
"""

def frequency_dict(elements: list) -> dict:
    diz = {}
    for element in elements:
        if element in diz:
            diz[element] += 1
        else:
            diz[element] = 1
    return diz

print(frequency_dict(['mela', 'banana', 'mela']))