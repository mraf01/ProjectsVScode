"""
Scrivi una funzione che ritorna il valore massimo, minimo e la media 
di una lista di numeri interi.
"""

def list_statistics(numbers: list[int]) -> float:     
    media = sum(numbers) / len(numbers)
    return max(numbers), min(numbers), media

print(list_statistics([1, 2, 3, 4, 5])) 