'''
Vogliamo gestire un contatore che può essere incrementato, decrementato, resettato e visualizzato. 
La classe offre un modo semplice per tenere traccia di un conteggio che non può diventare negativo.

Classe Contatore
Attributi:
- conteggio: un intero che conserva il valore del conteggio, inizializzato a 0.

Metodi:
- __init__(): Inizializza l'attributo conteggio a 0.
- setZero(): Imposta il conteggio a 0.
- add1(): Incrementa il conteggio di 1.
- sub1(): Decrementa il conteggio di 1, ma non permette che il conteggio diventi negativo. Se il conteggio è già 0, stampa un messaggio di errore.
- get(): Restituisce il valore corrente del conteggio.
- mostra(): Stampa a schermo il valore corrente del conteggio.
'''

class Contatore:
    def __init__(self):
        self.conteggio = 0

    def setZero(self):
        self.conteggio = 0

    def add1(self):
        self.conteggio += 1

    def sub1(self):
        if self.conteggio > 0:
            self.conteggio -= 1
        else:
            print("Non è possibile eseguire la sottrazione")

    def get(self):
        return self.conteggio

    def mostra(self):
        print(f"Conteggio attuale: {self.conteggio}")


# Test

c = Contatore()
c.add1()
c.mostra()  # output: Conteggio attuale: 1

c = Contatore()
c.add1()
c.add1()
c.add1()
c.mostra()  # output: Conteggio attuale: 3

c = Contatore()
c.sub1()    # output: Non è possibile eseguire la sottrazione
c.mostra()  # output: Conteggio attuale: 0

c = Contatore()
c.add1()
c.add1()
c.add1()
c.add1()
c.sub1()
c.add1()
c.add1()
c.sub1()
c.mostra()  # output: Conteggio attuale: 4

c = Contatore()
c.add1()
c.add1()
c.add1()
c.add1()
c.sub1()
c.add1()
c.add1()
z  = c.get()
print(z)  # output: 5

c = Contatore()
c.add1()
c.add1()
c.add1()
c.add1()
c.sub1()
c.add1()
c.setZero()
c.mostra()  # output: Conteggio attuale: 0
