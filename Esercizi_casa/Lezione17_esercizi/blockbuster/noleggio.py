class Noleggio:
    def __init__(self, film_list):
        self.film_list = film_list
        self.rented_film = {}

    def isAvaible(self, film):
        for f in self.film_list:
            if f.isEqual(film):
                print(f"Il film scelto è disponibile: {film.getTitle()}!")
                return True
        print(f"Il film scelto non è disponibile: {film.getTitle()}!")
        return False

    def rentAMovie(self, film, clientID):
        if self.isAvaible(film):
            new_film_list = []
            for f in self.film_list:
                if not f.isEqual(film):
                    new_film_list.append(f)
            self.film_list = new_film_list
            if clientID in self.rented_film:
                self.rented_film[clientID].append(film)
            else:
                self.rented_film[clientID] = [film]
            print(f"Il cliente {clientID} ha noleggiato {film.getTitle()}!")
        else:
            print(f"Non è possibile noleggiare il film {film.getTitle()}!")

    def giveBack(self, film, clientID, days):
        if clientID in self.rented_film and film in self.rented_film[clientID]:
            self.rented_film[clientID].remove(film)
            self.film_list.append(film)
            penale = film.calcolaPenaleRitardo(days)
            print(f"Cliente: {clientID}! La penale da pagare per il film {film.getTitle()} e' di {penale} euro!")

    def printMovies(self):
        for film in self.film_list:
            print(f"{film.getTitle()} - {film.getGenere()} -")

    def printRentMovies(self, clientID):
        if clientID in self.rented_film:
            for film in self.rented_film[clientID]:
                print(f"{film.getTitle()} - {film.getGenere()} -")