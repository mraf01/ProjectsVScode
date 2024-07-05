"""
Sistema di Prenotazione Cinema

Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. Il cinema ha diverse sale, 
ognuna con un diverso film in programmazione. Gli utenti possono vedere quali film sono disponibili e 
prenotare posti per un determinato spettacolo.
 
Classi:
- Film: Rappresenta un film con titolo e durata.
 
- Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.

Metodi:
    - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore.
    - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
- Cinema: Gestisce le operazioni legate alla gestione delle sale.

Metodi:
    - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
    - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.

Test case:

    Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
    Un cliente sceglie un film e prenota un certo numero di posti.
    Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.
"""

class Film:
    def __init__(self, titolo, durata):
        self.titolo = titolo
        self.durata = durata

class Sala:
    def __init__(self, numero, film, posti_totali):
        self.numero = numero
        self.film = film
        self.posti_totali = posti_totali
        self.posti_prenotati = 0
    
    def prenota_posti(self, num_posti):
        if self.posti_prenotati + num_posti <= self.posti_totali:
            self.posti_prenotati += num_posti
            return f"Prenotazione confermata per {num_posti} posti nella sala {self.numero} per il film {self.film.titolo}."
        else:
            posti_disponibili = self.posti_totali - self.posti_prenotati
            return f"Errore: Solo {posti_disponibili} posti disponibili nella sala {self.numero}."

    def posti_disponibili(self):
        return self.posti_totali - self.posti_prenotati

class Cinema:
    def __init__(self):
        self.sale = []
    
    def aggiungi_sala(self, sala):
        self.sale.append(sala)
    
    def prenota_film(self, titolo_film, num_posti):
        for sala in self.sale:
            if sala.film.titolo == titolo_film:
                return sala.prenota_posti(num_posti)
        return f"Errore: Film {titolo_film} non trovato."

# Test case
cinema = Cinema()

film1 = Film("Gladiator", 155)
film2 = Film("Avatar", 162)

sala1 = Sala(1, film1, 100)
sala2 = Sala(2, film2, 80)

cinema.aggiungi_sala(sala1)
cinema.aggiungi_sala(sala2)

print(cinema.prenota_film("Gladiator", 10))  # Prenotazione confermata per 10 posti
print(cinema.prenota_film("Spider-Man", 85))  # Errore: Solo 80 posti disponibili
print(cinema.prenota_film("Avatar", 95))  # Errore: Solo 90 posti disponibili
print(cinema.prenota_film("300: Rise of An Empire", 5))  # Errore: Film 300: Rise of An Empire non trovato