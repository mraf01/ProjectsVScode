'''
Esercizio: Codificatori di messaggio

# Codificatori Messaggio
Si crei una classe astratta chiamata CodificatoreMessaggio che ha un solo metodo astratto codifica(testoInChiaro), dove testoInChiaro sarà il messaggio da codificare. Il metodo restituirà il messaggio codificato.

Si crei una classe astratta chiamata DecodificatoreMessaggio che abbia un solo metodo decodifica(testoCodificato), dove testoCodificato sarà il messaggio da decodificare. Il metodo ritornerà il messaggio decodificato.

Si crei una classe CifratoreAScorrimento che implementa le classi astratte CodificatoreMessaggio e DecodificatoreMessaggio. Il costruttore dovrebbe ricevere un numero intero chiamato chiave. Si definisca il metodo codifica(testoInChiaro) così che ogni lettera del testo sia spostata dal valore contenuto in chiave.
Per esempio, se chiave è uguale a 3, la lettera 'a' sarà sostituita da 'd', la lettera 'b' sarà sostituita da 'e', la lettera 'c' sarà sostituita da 'f' e così via.
 Suggerimento: si potrebbe definire un metodo privato sposta_carattere(c) che restituisca la codifica di un singolo carattere c da concatenare agli altri per costruire il messaggio codificato nel metodo codifica(testoInChiaro).

Si crei una classe CifratoreACombinazione che implementa le classi astratte CodificatoreMessaggio e DecodificatoreMessaggio. Il costruttore dovrebbe ricevere un numero intero chiamato n. Si definisca il metodo codifica(testoInChiaro) così che il messaggio sia combinato n volte. Per eseguire una singola combinazione, si divide il messaggio a metà e poi si prendono i caratteri da ognuna delle metà in modo alternato. Per esempio, se il messaggio è 'abcdefghi', le metà sono 'abcde' e 'fghi' (nel caso in cui la lunghezza del testo da decifrare sia un numero dispari, la prima metà deve essere più lunga della seconda metà). Il messaggio combinato è 'afbgchdie'.
Suggerimento: si potrebbe definire un metodo privato combinazione(testo) che esegue la combinazione del testo e ritorni il testo cifrato da usare nel metodo codifica(testoInChiaro).

Si scriva il metodo decodifica(testoCodificato) per ognuna delle classi CifrarioAScorrimento e CifrarioACombinazione.

Suggerimento: definire il metodo privato decodifica_carattere() per la classe CifrarioAScorrimento che compie un'azione inversa al metodo sposta_carattere().
Suggerimento: definire il metodo privato decodifica_combinazione() per la classe CifrarioACombinazione che compie un'azione inversa al metodo combinazione().

Infine, si implementi anche un metodo per leggere il testo da cifrare da un file e un metodo per scrivere il testo cifrato su un file per entrambe le classi CifratoreAScorrimento e CifratoreACombinazione.

### Test tramite codice driver:
Test del Cifratore a Scorrimento:
- Inizializzazione: Viene creato un oggetto CifratoreAScorrimento con una chiave di scorrimento di 3.
- Lettura del testo: Il testo in chiaro viene letto da un file.
- Codifica: Il testo in chiaro viene codificato utilizzando il cifratore a scorrimento.
- Scrittura del testo codificato: Il testo codificato viene scritto su un file.
- Stampa del testo codificato: Il testo codificato viene stampato.
- Decodifica: Il testo codificato viene decodificato.
- Stampa del testo decodificato: Il testo decodificato viene stampato.

Test del Cifratore a Combinazione:
- Inizializzazione: Viene creato un oggetto CifratoreACombinazione con 3 combinazioni.
- Lettura del testo: Il testo in chiaro viene letto da un file.
- Codifica: Il testo in chiaro viene codificato utilizzando il cifratore a combinazione.
- Scrittura del testo codificato: Il testo codificato viene scritto su un file.
- Stampa del testo codificato: Il testo codificato viene stampato.
- Decodifica: Il testo codificato viene decodificato.
- Stampa del testo decodificato: Il testo decodificato viene stampato.
'''

from abc import ABC, abstractmethod

class CodificatoreMessaggio(ABC):
    @abstractmethod
    def codifica(self, testoInChiaro):
        pass

class DecodificatoreMessaggio(ABC):
    @abstractmethod
    def decodifica(self, testoCodificato):
        pass

class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, chiave):
        self.chiave = chiave

    def codifica(self, testoInChiaro):
        testo_codificato = ""
        for c in testoInChiaro:
            testo_codificato += self._sposta_carattere(c, self.chiave)
        return testo_codificato
    
    def decodifica(self, testoCodificato):
        testo_decodificato = ""
        for c in testoCodificato:
            testo_decodificato += self._sposta_carattere(c, -self.chiave)
        return testo_decodificato
    
    def _sposta_carattere(self, c, chiave):
        if c.isalpha():
            if c.islower():
                base = ord('a')
            else:
                base = ord('A')
            return chr((ord(c) - base + chiave) % 26 + base)
        else:
            return c


class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, n):
        self.n = n

    def codifica(self, testoInChiaro):
        testo = testoInChiaro
        for _ in range(self.n):
            testo = self._combinazione(testo)
        return testo
    
    def decodifica(self, testoCodificato):
        testo = testoCodificato
        for _ in range(self.n):
            testo = self._decodifica_combinazione(testo)
        return testo
    
    def _combinazione(self, testo):
        metà = (len(testo) + 1) // 2
        prima_metà = testo[:metà]
        seconda_metà = testo[metà:]
        combinato = ""
        min_len = min(len(prima_metà), len(seconda_metà))
        for i in range(min_len):
            combinato += prima_metà[i] + seconda_metà[i]
        if len(prima_metà) > min_len:
            combinato += prima_metà[min_len:]
        return combinato

    def _decodifica_combinazione(self, testo):
        metà = (len(testo) + 1) // 2
        prima_metà = ""
        seconda_metà = ""
        for i in range(metà):
            prima_metà += testo[2*i]
            if 2*i+1 < len(testo):
                seconda_metà += testo[2*i+1]
        return prima_metà + seconda_metà


def leggi_da_file(nome_file):
    with open(nome_file, 'r') as file:
        return file.read()

def scrivi_su_file(nome_file, testo):
    with open(nome_file, 'w') as file:
        file.write(testo)



# Test tramite codice driver:

# Test del Cifratore a Scorrimento
cifratore_scorrimento = CifratoreAScorrimento(3)
testo_in_chiaro = leggi_da_file('testo_in_chiaro.txt')
testo_codificato = cifratore_scorrimento.codifica(testo_in_chiaro)
scrivi_su_file('testo_codificato.txt', testo_codificato)
print("Testo Codificato (Scorrimento):", testo_codificato)
testo_decodificato = cifratore_scorrimento.decodifica(testo_codificato)
print("Testo Decodificato (Scorrimento):", testo_decodificato)

# Test del Cifratore a Combinazione
cifratore_combinazione = CifratoreACombinazione(3)
testo_in_chiaro = leggi_da_file('testo_in_chiaro.txt')
testo_codificato = cifratore_combinazione.codifica(testo_in_chiaro)
scrivi_su_file('testo_codificato.txt', testo_codificato)
print("Testo Codificato (Combinazione):", testo_codificato)
testo_decodificato = cifratore_combinazione.decodifica(testo_codificato)
print("Testo Decodificato (Combinazione):", testo_decodificato)