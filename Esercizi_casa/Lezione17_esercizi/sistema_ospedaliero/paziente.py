from persona import Persona

class Paziente(Persona):
    def __init__(self, first_name, last_name, idCode):
        super().__init__(first_name, last_name)
        self.__idCode = idCode

    def setIdCode(self, idCode):
        self.__idCode = idCode

    def getIdCode(self):
        return self.__idCode

    def patientInfo(self):
        print(f"Paziente: {self.getName()} {self.getLastname()}\nID: {self.__idCode}")