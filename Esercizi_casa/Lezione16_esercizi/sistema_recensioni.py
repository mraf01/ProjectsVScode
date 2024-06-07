'''
Sistema di Recensioni

Obiettivo:
Implementare una classe Media che rappresenti un media generico (ad esempio, un film o un libro) e una classe derivata 
Film che rappresenti specificamente un film. Gli studenti dovranno anche creare oggetti di queste classi, 
aggiungere valutazioni e visualizzare le recensioni.
Specifiche della Classe Media:
 
Attributi:
- title (stringa): Il titolo del media.
- reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5, 
dove 1=Terribile, 2=Brutto, 3=Normale, 4=Bello, 5=Grandioso.
Metodi:
- set_title(self, title): Imposta il titolo del media.
- get_title(self): Restituisce il titolo del media.
- aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
- getMedia(self): Calcola e restituisce la media delle valutazioni.
- getRate(self): Restituisce una stringa che descrive il giudizio medio basato sulla media delle valutazioni, 
ovvero mostra "Terribile" se il voto medio si avvicina a 1, "Brutto" se il voto medio si avvicina a 2, 
"Normale" se il voto medio si avvicina a 3, "Bello" se il voto medio si avvicina a 4, "Grandioso" se il voto medio si avvicina a 5.
- ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
- recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo, il voto medio, 
il giudizio e le percentuali di ciascun voto. Esempio di riassunto:
 
Titolo del Film: The Shawshank Redemption
Voto Medio: 3.80
Giudizio: Bello
Terribile: 10.00%
Brutto: 10.00%
Normale: 10.00%
Bello: 30.00%
Grandioso: 40.00%
Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film, 
aggiunga a ognuno dei due almeno dieci valutazioni e richiami il metodo recensione().
'''

class Media:
    def __init__(self):
        self.reviews: list[int] = []

    def set_title(self, title: str) -> None:
        self.title = title

    def get_title(self) -> str:
        return self.title

    def aggiungiValutazione(self, voto: int) -> None:
        if voto >= 1 and voto <= 5:
            self.reviews.append(voto)

    def getMedia(self) -> float:
        if self.reviews:
            totale: int = sum(self.reviews)
            conteggio: int = len(self.reviews)
            media: float = totale / conteggio
            return media
        else:
            return 0
        
        # return sum(self.reviews) / len(self.reviews) if self.reviews else 0

    def getRate(self) -> str:
        media = self.getMedia()
        if media >= 4.5:
            return "Grandioso"
        elif media >= 3.5:
            return "Bello"
        elif media >= 2.5:
            return "Normale"
        elif media >= 1.5:
            return "Brutto"
        else:
            return "Terribile"
        
        # media = round(self.getMedia())
        # return ["Terribile", "Brutto", "Normale", "Bello", "Grandioso"][media - 1]

    def ratePercentage(self, voto: int) -> float:
        if self.reviews:
            numero_di_voti: int = self.reviews.count(voto)
            totale_recensioni: int = len(self.reviews)
            percentuale: float = (numero_di_voti / totale_recensioni) * 100
            return percentuale
        else:
            return 0
        
        # return self.reviews.count(voto) / len(self.reviews) * 100 if self.reviews else 0

    def recensione(self) -> None:
        print(f"Titolo del Film: {self.get_title()}")
        print(f"Voto Medio: {self.getMedia()}")
        print(f"Giudizio: {self.getRate()}")
        for i in range(1, 6):
            print(f"Voto {i}: {self.ratePercentage(i)}%")

class Film(Media):
    def __init__(self, title: str):
        super().__init__()
        self.set_title(title)

film1: Film = Film("The Shawshank Redemption")
film2: Film = Film("Gladiator")

for voto in [5, 4, 3, 5, 4, 5, 4, 3, 5, 4]:
    film1.aggiungiValutazione(voto)
    film2.aggiungiValutazione(voto)

film1.recensione()
film2.recensione()
