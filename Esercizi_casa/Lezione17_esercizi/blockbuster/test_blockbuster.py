import unittest
from film import Film
from movie_genre import Azione, Commedia, Drama
from noleggio import Noleggio

class TestFilm(unittest.TestCase):
    def setUp(self):
        self.films = [
            Azione(1, "Azione1"), Azione(2, "Azione2"), Azione(3, "Azione3"),
            Azione(4, "Azione4"), Azione(5, "Azione5"),
            Commedia(6, "Commedia1"), Commedia(7, "Commedia2"),
            Commedia(8, "Commedia3"), Commedia(9, "Commedia4"),
            Drama(10, "Drama1")
        ]
        self.noleggio = Noleggio(self.films.copy())

    def test_isAvaible(self):
        film = self.films[0]
        self.assertTrue(self.noleggio.isAvaible(film))
        self.noleggio.rentAMovie(film, 100)
        self.assertFalse(self.noleggio.isAvaible(film))

    def test_rentAMovie(self):
        film = self.films[0]
        self.noleggio.rentAMovie(film, 100)
        self.assertFalse(self.noleggio.isAvaible(film))
        self.assertIn(film, self.noleggio.rented_film[100])

    def test_rentUnavailableMovie(self):
        film = self.films[0]
        self.noleggio.rentAMovie(film, 100)
        self.noleggio.rentAMovie(film, 101)
        self.assertNotIn(film, self.noleggio.rented_film.get(101, []))

    def test_giveBack(self):
        film = self.films[0]
        self.noleggio.rentAMovie(film, 100)
        self.noleggio.giveBack(film, 100, 5)
        self.assertTrue(self.noleggio.isAvaible(film))
        self.assertNotIn(film, self.noleggio.rented_film.get(100, []))

    def test_calcolaPenaleRitardo(self):
        film_azione = self.films[0]
        self.assertEqual(film_azione.calcolaPenaleRitardo(3), 9.0)
        film_commedia = self.films[5]
        self.assertEqual(film_commedia.calcolaPenaleRitardo(3), 7.5)
        film_drama = self.films[9]
        self.assertEqual(film_drama.calcolaPenaleRitardo(3), 6.0)

    def test_printMovies(self):
        self.noleggio.printMovies()

    def test_printRentMovies(self):
        film = self.films[0]
        self.noleggio.rentAMovie(film, 100)
        self.noleggio.printRentMovies(100)

if __name__ == "__main__":
    unittest.main()