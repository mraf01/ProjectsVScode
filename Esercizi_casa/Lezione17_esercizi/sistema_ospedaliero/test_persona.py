import unittest
from persona import Persona
from dottore import Dottore
from paziente import Paziente
from fatture import Fattura

class TestPersona(unittest.TestCase):
    def setUp(self):
        self.persona = Persona("Mario", "Rossi")

    def test_initialization(self):
        self.assertEqual(self.persona.getName(), "Mario")
        self.assertEqual(self.persona.getLastname(), "Rossi")
        self.assertEqual(self.persona.getAge(), 0)

    def test_setName(self):
        self.persona.setName("Luigi")
        self.assertEqual(self.persona.getName(), "Luigi")
        self.persona.setName(123)
        self.assertNotEqual(self.persona.getName(), 123)

    def test_setLastName(self):
        self.persona.setLastName("Verdi")
        self.assertEqual(self.persona.getLastname(), "Verdi")
        self.persona.setLastName(123)
        self.assertNotEqual(self.persona.getLastname(), 123)

    def test_setAge(self):
        self.persona.setAge(25)
        self.assertEqual(self.persona.getAge(), 25)
        self.persona.setAge("venti")
        self.assertNotEqual(self.persona.getAge(), "venti")

class TestDottore(unittest.TestCase):
    def setUp(self):
        self.dottore = Dottore("Mario", "Rossi", "Pediatra", 50.0)
        self.dottore.setAge(40)

    def test_initialization(self):
        self.assertEqual(self.dottore.getSpecialization(), "Pediatra")
        self.assertEqual(self.dottore.getParcel(), 50.0)

    def test_isValidDoctor(self):
        self.assertTrue(self.dottore.isAValidDoctor())
        self.dottore.setAge(28)
        self.assertFalse(self.dottore.isAValidDoctor())

class TestPaziente(unittest.TestCase):
    def setUp(self):
        self.paziente = Paziente("Luca", "Bianchi", "ABC123")

    def test_initialization(self):
        self.assertEqual(self.paziente.getIdCode(), "ABC123")

class TestFattura(unittest.TestCase):
    def setUp(self):
        self.dottore = Dottore("Mario", "Rossi", "Pediatra", 50.0)
        self.dottore.setAge(40)
        self.pazienti = [Paziente("Luca", "Bianchi", "ABC123"), Paziente("Anna", "Neri", "XYZ789")]
        self.fattura = Fattura(self.pazienti, self.dottore)

    def test_initialization(self):
        self.assertEqual(self.fattura.getFatture(), 2)
        self.assertEqual(self.fattura.getSalary(), 100.0)

    def test_addPatient(self):
        new_patient = Paziente("Giulia", "Verdi", "LMN456")
        self.fattura.addPatient(new_patient)
        self.assertEqual(self.fattura.getFatture(), 3)
        self.assertEqual(self.fattura.getSalary(), 150.0)

    def test_removePatient(self):
        self.fattura.removePatient("ABC123")
        self.assertEqual(self.fattura.getFatture(), 1)
        self.assertEqual(self.fattura.getSalary(), 50.0)

if __name__ == "__main__":
    unittest.main()