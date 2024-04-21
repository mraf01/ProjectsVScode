def diff_cum(l: list[float]) -> float:
    # esempio: 
    # l = [1,2,3,4,5,6]
    # deve restituire 1-2-3-4-5-6 = -19

    diff: float = l[0]
    for i in l[1:]:
        diff -= i
    return diff

    # oppure

    diff: float = l[0]
    for i in range(1, len(l)):
      diff -= l[i] 
    return diff


lista: list[float] = [1,2,3,4,5,6]
result: float = diff_cum(lista)
print(f"Il risultato della differenza è {result}")

