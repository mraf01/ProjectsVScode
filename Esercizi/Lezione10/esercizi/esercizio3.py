'''
Sviluppare una funzione in Python per calcolare lo stipendio lordo di ciascuno dei diversi impiegati. 
L'azienda paga 10 dollari all'ora per le prime 40 ore di lavoro e paga "una volta e mezza" 
la paga oraria per tutte le ore di lavoro oltre le 40 ore.
 
Per ogni operaio, viene fornito il numero di ore che tale impiegato ha lavorato durante la settimana.
La vostra funzione deve ricevere questa informazione per ogni impiegato e determinare e stampare lo stipendio lordo.
'''

def calcola_stipendio(ore_lavorate: int) -> float:
    paga = 10.0
    ore = 40.0
    stipendio_totale = 0.0
    if ore_lavorate <= ore:
        stipendio_totale = ore_lavorate * paga
    else:
        stipendio_totale = ore * paga
        ore_straordinario = ore_lavorate - ore
        stipendio_straordinario = ore_straordinario * paga * 1.5
        stipendio_totale += stipendio_straordinario
    return stipendio_totale


# Test
print(calcola_stipendio(40))  # output: 400.0
print(calcola_stipendio(30))  # output: 300.0
print(calcola_stipendio(45))  # output: 475.0
print(calcola_stipendio(60))  # output: 700.0
print(calcola_stipendio(0))  # output: 0.0