def diff_cum(l: list[float], index: int) -> float:
    # esempio:
    # l = [1, 2, 3, 4, 5, 6]
    # indice = 2
    # deve restituire 3-1-2-4-5-6 = -15

    if -len(l) <= index < len(l): # o  index < len(l) and index >= -len(l)   Verifica se l'indice è valido
        fulcro = l[index]
        for i in range(len(l)):
            if i != index:
                fulcro -= l[i]
        return fulcro
    else:
        return 70  # Restituisce un valore arbitrario per l'indice fuori limite
    
    # oppure

    if -len(l) <= index < len(l):
        fulcro = l[index]
        for i in range(len(l)):
            if i == index:
                continue  # Salta l'iterazione corrente se i è uguale all'indice
            fulcro -= l[i]
        return fulcro
    else:
        return 70

    # oppure

    if -len(l) <= index < len(l):
        fulcro = l.pop(index)
        for i in range(len(l)):
            fulcro -= l[i]
        return fulcro
    else:
        return 70

    # oppure

    if -len(l) <= index < len(l):  
        return l[index] - sum(l[:index] + l[index+1:]) 
    else:
        return 70 


lista: list[float] = [1, 2, 3, 4, 5, 6]
indice: int = 2
result: float = diff_cum(lista, indice)
print(f"Il risultato della differenza è {result}")

