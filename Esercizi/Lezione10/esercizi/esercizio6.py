'''
Definire una funzione chiamata hypotenuse che calcoli la lunghezza dell'ipotenusa di un triangolo rettangolo. 
La funzione deve ricevere due argomenti di tipo float (corrispondenti ai due lati del triangolo) e restituire l'ipotenusa come un float.

Per calcolare l'ipotenusa, si può ricorrere al teorema di Pitagora.
'''

def hypotenuse(a: float, b: float) -> float:
    ipotenusa = (a**2 + b**2)**0.5
    return ipotenusa

# Test
print(hypotenuse(3.0, 4.0))  # output: 5.0
print(hypotenuse(5.0, 12.0))  # output: 13.0
print(hypotenuse(8.0, 15.0))  # output: 17.0
print(hypotenuse(7.0, 24.0))  # output: 25.0