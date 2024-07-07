from abc import ABC, abstractmethod

class Forma(ABC):
    def __init__(self, nome):
        self.nome = nome
    
    @abstractmethod
    def get_area(self):
        pass
    
    @abstractmethod
    def render(self):
        pass

class Quadrato(Forma):
    def __init__(self, lato):
        super().__init__("Quadrato")
        self.lato = lato
    
    def get_area(self):
        return self.lato ** 2
    
    def render(self):
        print(f"Ecco un Quadrato di lato {self.lato}!\n")
        for i in range(self.lato):
            for j in range(self.lato):
                if i == 0 or i == self.lato - 1 or j == 0 or j == self.lato - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        print(f"L'area di questo quadrato vale: {self.get_area()}\n")

class Rettangolo(Forma):
    def __init__(self, base, altezza):
        super().__init__("Rettangolo")
        self.base = base
        self.altezza = altezza
    
    def get_area(self):
        return self.base * self.altezza
    
    def render(self):
        print(f"Ecco un Rettangolo avente base {self.base} ed altezza {self.altezza}!\n")
        for i in range(self.altezza):
            for j in range(self.base):
                if i == 0 or i == self.altezza - 1 or j == 0 or j == self.base - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        print(f"L'area di questo rettangolo vale: {self.get_area()}\n")

class Triangolo(Forma):
    def __init__(self, lato):
        super().__init__("Triangolo")
        self.lato = lato
    
    def get_area(self):
        return (self.lato ** 2) / 2
    
    def render(self):
        print(f"Ecco un Triangolo avente base {self.lato} ed altezza {self.lato}!\n")
        for i in range(self.lato):
            for j in range(i + 1):
                if i == self.lato - 1 or j == 0 or j == i:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        print(f"L'area di questo triangolo vale: {self.get_area()}\n")


if __name__ == "__main__":
    quadrato = Quadrato(4)
    quadrato.render()

    rettangolo = Rettangolo(8, 4)
    rettangolo.render()

    triangolo = Triangolo(4)
    triangolo.render()