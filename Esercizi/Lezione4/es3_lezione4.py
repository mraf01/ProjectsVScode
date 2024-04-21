def median(l: list[float]) -> float:
    """
        Questa funzione prende in input una lista di numeri reali
        e restituisce la mediana di questa lista

        Esempio:
            l = [2,9,0,-1,25,2,4,3] (lunghezza pari)
            l ordinata: -1 0 2 2 3 4 9 25
            mediana = (2 + 3)/2 = 2.5

            l = [2,9,0,-1,25,2,4] (lunghezza dispari)
            l ordinata: -1 0 2 2 4 9 25
            mediana = 2 perchè 2 è l'elemento centrale
    """
    
    l.sort()
    mid = len(l) // 2
    # [1,2,3,4 , 5,6,7,8]
    # se len(l) = 8, mid = 4

    mediana: float = 0
    if len(l) % 2 == 1: # dispari
        mediana = l[mid]
    else: # pari
        mediana = (l[mid] + l[mid - 1]) / 2
    return mediana

lista = [2,9,0,-1,25,2,4,3]
mediana = median(lista)
print(f"La mediana della lista {lista} è {mediana}")
