import os

class Documento:
    def __init__(self, testo=""):
        self.testo = testo
    
    def getText(self):
        return self.testo
    
    def setText(self, testo):
        self.testo = testo
    
    def isInText(self, keyword):
        return keyword in self.testo

class Email(Documento):
    def __init__(self, mittente="", destinatario="", titolo="", testo=""):
        super().__init__(testo)
        self.mittente = mittente
        self.destinatario = destinatario
        self.titolo = titolo
    
    def getMittente(self):
        return self.mittente
    
    def setMittente(self, mittente):
        self.mittente = mittente
    
    def getDestinatario(self):
        return self.destinatario
    
    def setDestinatario(self, destinatario):
        self.destinatario = destinatario
    
    def getTitolo(self):
        return self.titolo
    
    def setTitolo(self, titolo):
        self.titolo = titolo
    
    def getText(self):
        return f"Da: {self.mittente}, A: {self.destinatario}\nTitolo: {self.titolo}\nMessaggio: {self.testo}"
    
    def writeToFile(self, percorso):
        with open(percorso, 'w') as file:
            file.write(self.getText())

class File(Documento):
    def __init__(self, nomePercorso):
        super().__init__()
        self.nomePercorso = nomePercorso
        self.leggiTestoDaFile()
    
    def leggiTestoDaFile(self):
        with open(self.nomePercorso, 'r') as file:
            self.testo = file.read()
    
    def getText(self):
        return f"Percorso: {self.nomePercorso}\nContenuto: {self.testo}"