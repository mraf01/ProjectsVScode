"""
Sistema di Gestione Biblioteca

Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. 
Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi. 
Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli, 
restituirli e visualizzare quali libri sono disponibili in un dato momento.
 
Classi:
- Libro: Rappresenta un libro con titolo, autore, stato del prestito. Il libro deve essere inizialmente disponibile (non prestato).

- Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

    Metodi:
    - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce un messaggio di conferma.

    - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile. 
      Restituisce un messaggio di stato.

    - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. 
      Restituisce un messaggio di stato.

    - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. 
      Se non ci sono libri disponibili, restituisce un messaggio di errore.

Test Cases:
- Un amministratore della biblioteca aggiunge alcuni libri all'inventario.
- Un utente prende in prestito un libro, che viene quindi marcato come non disponibile.
- L'utente restituisce il libro, che viene marcato di nuovo come disponibile.
- In qualsiasi momento, un utente può visualizzare quali libri sono disponibili per il prestito.
"""

class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
        self.prestato = False

class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def aggiungi_libro(self, libro):
        self.catalogo.append(libro)
        return f'Libro "{libro.titolo}" di {libro.autore} aggiunto al catalogo.'

    def presta_libro(self, titolo):
        for libro in self.catalogo:
            if libro.titolo == titolo:
                if not libro.prestato:
                    libro.prestato = True
                    return f'Libro "{titolo}" prestato con successo.'
                else:
                    return f'Libro "{titolo}" già prestato.'
        return f'Libro "{titolo}" non trovato nel catalogo.'

    def restituisci_libro(self, titolo):
        for libro in self.catalogo:
            if libro.titolo == titolo:
                if libro.prestato:
                    libro.prestato = False
                    return f'Libro "{titolo}" restituito con successo.'
                else:
                    return f'Libro "{titolo}" non era prestato.'
        return f'Libro "{titolo}" non trovato nel catalogo.'

    def mostra_libri_disponibili(self):
        disponibili = [libro.titolo for libro in self.catalogo if not libro.prestato]
        if disponibili:
            return disponibili
        else:
            return 'Nessun libro disponibile.'

# Test cases
biblioteca = Biblioteca()
print(biblioteca.aggiungi_libro(Libro("Il Signore degli Anelli", "J.R.R. Tolkien")))
print(biblioteca.aggiungi_libro(Libro("1984", "George Orwell")))
print(biblioteca.aggiungi_libro(Libro("Il Piccolo Principe", "Antoine de Saint-Exupéry")))

print(biblioteca.presta_libro("1984"))
print(biblioteca.mostra_libri_disponibili())

print(biblioteca.restituisci_libro("1984"))
print(biblioteca.mostra_libri_disponibili())