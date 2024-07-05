"""
Catalogo Film

Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere, 
rimuovere e cercare film di un particolare regista. Il sistema dovrebbe consentire anche di visualizzare tutti i registi e i loro film.

Classe:
- MovieCatalog: Gestisce tutte le operazioni legate al catalogo dei film.

    Metodi:
    - add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo. 
      Se il regista non esiste, viene creato un nuovo record. Se il regista esiste, la sua lista di film viene aggiornata.

    - remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di un regista. 
      Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.

    - list_directors(): Elenca tutti i registi presenti nel catalogo.

    - get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.

    - search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo. 
      Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata o 
      un messaggio di errore se nessun film contiene la parola cercata nel titolo.
"""

class MovieCatalog:
    def __init__(self):
        self.catalog = {}

    def add_movie(self, director_name, movies):
        if director_name not in self.catalog:
            self.catalog[director_name] = []
        self.catalog[director_name].extend(movies)
        return f'Film aggiunti per il regista {director_name}.'

    def remove_movie(self, director_name, movie_name):
        if director_name in self.catalog:
            if movie_name in self.catalog[director_name]:
                self.catalog[director_name].remove(movie_name)
                if not self.catalog[director_name]:
                    del self.catalog[director_name]
                return f'Film "{movie_name}" rimosso dal catalogo di {director_name}.'
            else:
                return f'Film "{movie_name}" non trovato per il regista {director_name}.'
        else:
            return f'Regista "{director_name}" non trovato nel catalogo.'

    def list_directors(self):
        return list(self.catalog.keys())

    def get_movies_by_director(self, director_name):
        if director_name in self.catalog:
            return self.catalog[director_name]
        else:
            return f'Regista "{director_name}" non trovato nel catalogo.'

    def search_movies_by_title(self, title):
        result = {}
        for director, movies in self.catalog.items():
            filtered_movies = []
            for movie in movies:
                if title.lower() in movie.lower():
                    filtered_movies.append(movie)
            if filtered_movies:
                result[director] = filtered_movies
        if result:
            return result
        else:
            return f'Nessun film trovato con il titolo contenente "{title}".'


# Test cases
movie_catalog = MovieCatalog()
print(movie_catalog.add_movie("Christopher Nolan", ["Inception", "Interstellar", "Dunkirk"]))
print(movie_catalog.add_movie("Quentin Tarantino", ["Pulp Fiction", "Kill Bill", "Inglourious Basterds"]))

print(movie_catalog.remove_movie("Quentin Tarantino", "Kill Bill"))
print(movie_catalog.list_directors())

print(movie_catalog.get_movies_by_director("Christopher Nolan"))
print(movie_catalog.search_movies_by_title("Dunkirk"))
print(movie_catalog.search_movies_by_title("Avatar"))