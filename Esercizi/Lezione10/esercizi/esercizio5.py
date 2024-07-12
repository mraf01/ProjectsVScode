'''
Scrivere una funzione chiamata integerPower che, dati in input una base e un esponente, 
restituisca il risultato della potenza base^exponent. 
Supporre che base sia un numero intero e che l'esponente sia un valore intero positivo e diverso da 0.
 
La funzione deve usare un ciclo come struttura di controllo per il calcolo del risultato.
Non utilizzare nessuna funzione della libreria math!
'''

def integerPower(base: int, exponent: int) -> int:
    result = 1
    for _ in range(exponent):
        result *= base
    return result

# Test	
print(integerPower(3, 4))  # output: 81
print(integerPower(5, 3))  # output: 125
print(integerPower(2, 5))  # output: 32
print(integerPower(10, 2))  # output: 100