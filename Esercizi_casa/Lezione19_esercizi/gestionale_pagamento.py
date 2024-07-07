from abc import ABC, abstractmethod

class Pagamento:
    def __init__(self):
        self.__importo = 0.0
    
    def set_importo(self, importo):
        if importo >= 0:
            self.__importo = float(importo)
    
    def get_importo(self):
        return self.__importo
    
    def dettagli_pagamento(self):
        return f"Importo del pagamento: €{self.__importo:.2f}"

class PagamentoContanti(Pagamento):
    def __init__(self, importo):
        super().__init__()
        self.set_importo(importo)
    
    def dettagli_pagamento(self):
        return f"Pagamento in contanti di: €{self.get_importo():.2f}"
    
    def in_pezzi_da(self):
        importo = self.get_importo()
        pezzi = {
            "banconote da 500 euro": 500,
            "banconote da 200 euro": 200,
            "banconote da 100 euro": 100,
            "banconote da 50 euro": 50,
            "banconote da 20 euro": 20,
            "banconote da 10 euro": 10,
            "banconote da 5 euro": 5,
            "monete da 2 euro": 2,
            "monete da 1 euro": 1,
            "monete da 0.5 euro": 0.5,
            "monete da 0.2 euro": 0.2,
            "monete da 0.1 euro": 0.1,
            "monete da 0.05 euro": 0.05,
            "monete da 0.01 euro": 0.01
        }
        
        risultato = []
        for pezzo, valore in pezzi.items():
            quantita = int(importo // valore)
            if quantita > 0:
                risultato.append(f"{quantita} {pezzo}")
                importo -= quantita * valore
                importo = round(importo, 2)
        return risultato

class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, importo, nome, data_scadenza, numero_carta):
        super().__init__()
        self.set_importo(importo)
        self.nome = nome
        self.data_scadenza = data_scadenza
        self.numero_carta = numero_carta
    
    def dettagli_pagamento(self):
        return (f"Pagamento di: €{self.get_importo():.2f} effettuato con la carta di credito\n"
                f"Nome sulla carta: {self.nome}\n"
                f"Data di scadenza: {self.data_scadenza}\n"
                f"Numero della carta: {self.numero_carta}")


if __name__ == "__main__":
    pagamento_contanti1 = PagamentoContanti(150.00)
    pagamento_contanti2 = PagamentoContanti(95.25)

    pagamento_carta1 = PagamentoCartaDiCredito(200.00, "Mario Rossi", "12/24", "1234567890123456")
    pagamento_carta2 = PagamentoCartaDiCredito(500.00, "Fabio Verdi", "01/25", "6543210987654321")

    print(pagamento_contanti1.dettagli_pagamento())
    print("\n".join(pagamento_contanti1.in_pezzi_da()))
    print()

    print(pagamento_contanti2.dettagli_pagamento())
    print("\n".join(pagamento_contanti2.in_pezzi_da()))
    print()

    print(pagamento_carta1.dettagli_pagamento())
    print()
    print(pagamento_carta2.dettagli_pagamento())
    print()