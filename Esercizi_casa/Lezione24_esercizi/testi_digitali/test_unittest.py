import unittest
from documento import Documento, Email, File
import os

class TestDocumento(unittest.TestCase):
    def test_get_set_text(self):
        doc = Documento()
        doc.setText("Hello")
        self.assertEqual(doc.getText(), "Hello")
    
    def test_is_in_text(self):
        doc = Documento("This is a sample text.")
        self.assertTrue(doc.isInText("sample"))
        self.assertFalse(doc.isInText("notpresent"))

class TestEmail(unittest.TestCase):
    def setUp(self):
        self.email = Email(mittente="mario@example.com", destinatario="fabio@example.com", titolo="Incontro", testo="Ciao Fabio, possiamo incontrarci domani?")
    
    def test_get_text(self):
        expected_text = "Da: mario@example.com, A: fabio@example.com\nTitolo: Incontro\nMessaggio: Ciao Fabio, possiamo incontrarci domani?"
        self.assertEqual(self.email.getText(), expected_text)
    
    def test_write_to_file(self):
        self.email.writeToFile("email1.txt")
        with open("email1.txt", 'r') as file:
            content = file.read()
        expected_text = "Da: mario@example.com, A: fabio@example.com\nTitolo: Incontro\nMessaggio: Ciao Fabio, possiamo incontrarci domani?"
        self.assertEqual(content, expected_text)
        os.remove("email1.txt")
    
    def test_is_in_text(self):
        self.assertTrue(self.email.isInText("incontrarci"))
        self.assertFalse(self.email.isInText("nonpresente"))

class TestFile(unittest.TestCase):
    def setUp(self):
        self.file_path = "document.txt"
        with open(self.file_path, 'w') as file:
            file.write("Questo e' il contenuto del file.")
        self.file_document = File(self.file_path)
    
    def test_get_text(self):
        expected_text = f"Percorso: {self.file_path}\nContenuto: Questo e' il contenuto del file."
        self.assertEqual(self.file_document.getText(), expected_text)
    
    def test_is_in_text(self):
        self.assertTrue(self.file_document.isInText("contenuto"))
        self.assertFalse(self.file_document.isInText("nonpresente"))
    
    def tearDown(self):
        os.remove(self.file_path)

if __name__ == '__main__':
    unittest.main()