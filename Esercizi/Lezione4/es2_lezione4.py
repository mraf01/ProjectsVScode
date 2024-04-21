def rewrite_dict(d: dict[str, int]) -> dict[str,int]:
    """
        Questa funzione prende in input un dizionario
        (e.s. d = {"ciao": 2, "hello": 3}) e restituisce
        un nuovo dizionario fatto così:
        d1 = {"ciao: 2/5, "hello": 3/5} dove 5 è la somma
        dei valori di d, ossia 2 + 3 = 5 
    """

    somma: float = sum(d.values()) 
    d1 = {} 
    for k, v in d.items(): 
        d1[k] = v/somma
    return d1

diz: dict[str, int] = {"ciao": 2, "hello": 3}
diz_nuovo: dict[str, float] = rewrite_dict(diz) 
print(f"L'output è: {diz_nuovo}") 

