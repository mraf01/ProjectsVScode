"""
Gestione di un magazzino

Scrivi un programma in Python che gestisca un magazzino. Il programma deve permettere di aggiungere prodotti al magazzino, 
cercare prodotti per nome e verificare la disponibilità di un prodotto.

Definisci una classe Prodotto con i seguenti attributi:
- nome (stringa)
- quantità (intero)
 
Definisci una classe Magazzino con i seguenti metodi:
- aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
- cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
- verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
 
Test case:

    Un gestore del magazzino crea un magazzino e diversi prodotti in diverse quantità. Successivamente, aggiunge i prodotti al magazzino.
    Il sistema cerca un prodotto per verificare se esiste nell'inventario.
    Il sistema verifica la disponibilità dei prodotti in inventario.
"""

class Prodotto:
    def __init__(self, nome, quantita):
        self.nome = nome
        self.quantita = quantita

class Magazzino:
    def __init__(self):
        self.prodotti = {}
    
    def aggiungi_prodotto(self, prodotto):
        if prodotto.nome in self.prodotti:
            self.prodotti[prodotto.nome].quantita += prodotto.quantita
        else:
            self.prodotti[prodotto.nome] = prodotto
    
    def cerca_prodotto(self, nome):
        if nome in self.prodotti:
            return self.prodotti[nome]
        else:
            return None
    
    def verifica_disponibilita(self, nome):
        prodotto = self.cerca_prodotto(nome)
        if prodotto:
            return f"{nome} è disponibile con una quantità di {prodotto.quantita}."
        else:
            return f"{nome} non è disponibile nel magazzino."

# Test case
magazzino = Magazzino()

prodotto1 = Prodotto("Laptop", 10)
prodotto2 = Prodotto("Mouse", 50)
prodotto3 = Prodotto("Tastiera", 30)

magazzino.aggiungi_prodotto(prodotto1)
magazzino.aggiungi_prodotto(prodotto2)
magazzino.aggiungi_prodotto(prodotto3)

print(magazzino.cerca_prodotto("Mouse"))

print(magazzino.verifica_disponibilita("Laptop"))
print(magazzino.verifica_disponibilita("Monitor"))