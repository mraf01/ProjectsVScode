from dottore import Dottore
from paziente import Paziente

class Fattura:
    def __init__(self, patients, doctor):
        if doctor.isAValidDoctor():
            self.__patients = patients
            self.__doctor = doctor
            self.__fatture = len(patients)
            self.__salary = 0
        else:
            self.__patients = None
            self.__doctor = None
            self.__fatture = None
            self.__salary = None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")

    def getSalary(self):
        if self.__doctor and self.__patients is not None:
            self.__salary = self.__doctor.getParcel() * self.__fatture
        return self.__salary

    def getFatture(self):
        if self.__patients is not None:
            self.__fatture = len(self.__patients)
        return self.__fatture

    def addPatient(self, newPatient):
        if self.__patients is not None:
            self.__patients.append(newPatient)
            self.getFatture()
            self.getSalary()
            print(f"Alla lista del Dottor {self.__doctor.getLastname()} è stato aggiunto il paziente {newPatient.getIdCode()}")

    def removePatient(self, idCode):
        if self.__patients is not None:
            for patient in self.__patients:
                if patient.getIdCode() == idCode:
                    self.__patients.remove(patient)
                    self.getFatture()
                    self.getSalary()
                    print(f"Alla lista del Dottor {self.__doctor.getLastname()} è stato rimosso il paziente {idCode}")
                    break