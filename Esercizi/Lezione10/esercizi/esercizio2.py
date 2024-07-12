'''
Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
- se x è pari, deve essere diviso per 2;
- se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1.
'''

def transform(x: int) -> int:
    if x % 2 == 0:
        return x // 2
    else:
        return (x * 3) - 1
    
# Test
print(transform(4))  # output: 2
print(transform(3))  # output: 8
print(transform(0))  # output: 0
print(transform(-10))  # output: -5
print(transform(-5))  # output: -16