s: str = "La meccanica quantistica è la teoria fisica che descrive il comportamento della materia, della radiazione e le reciproche interazioni, con particolare riguardo ai fenomeni caratteristici della scala di lunghezza o di energia atomica e subatomica,[2] dove le precedenti teorie classiche risultano inadeguate. Come caratteristica fondamentale, la meccanica quantistica descrive la radiazione[3] e la materia[4] sia come fenomeni ondulatori che come entità particellari, al contrario della meccanica classica, che descrive la luce solamente come un'onda e, ad esempio, l'elettrone solo come una particella. Questa inaspettata e controintuitiva proprietà della realtà fisica, chiamata dualismo onda-particella,[5] è la principale ragione del fallimento delle teorie sviluppate fino al XIX secolo nella descrizione degli atomi e delle molecole. La relazione tra natura ondulatoria e corpuscolare è enunciata nel principio di complementarità e formalizzata nel principio di indeterminazione di Heisenberg. Esistono numerosi formalismi matematici equivalenti della teoria, come la meccanica ondulatoria e la meccanica delle matrici; al contrario, ne esistono numerose e discordanti interpretazioni riguardo all'essenza ultima del cosmo e della natura, che hanno dato vita a un dibattito tuttora aperto nell'ambito della filosofia della scienza. La meccanica quantistica rappresenta, assieme alla teoria della relatività, uno spartiacque rispetto alla fisica classica, portando alla nascita della fisica moderna. Attraverso la teoria quantistica dei campi, generalizzazione della formulazione originale che include il principio di relatività ristretta, essa è a fondamento di molte altre branche della fisica, come la fisica atomica, la fisica della materia condensata, la fisica nucleare, la fisica delle particelle, la chimica quantistica."

def counter(s: str) -> list[int]:
    
    """
        Questa funzione prende una stringa in input e
        restituisce una lista costruita nel modo seguente:
        - il primo elemento della lista contiene il numero di caratteri nella stringa
        - il secondo elemento della lista contiene il numero di parole nella stringa
        - il terzo elemento della lista contiene il numero di parole distinte nella stringa
        - il quarto elemento della lista contiene il numero di frasi nella stringa
    """
    
    s = s.lower()
    res: list[int] = []
    # quanti caratteri ha la stringa
    res.append(len(s))
    # primo = len(s)
    # quante parole ha la stringa
    res.append(len(s.split())) # s = "ciao bello." -> s.split() -> ["ciao", "bello."]
    # secondo = len(s.split())
    # quante parole distinte ha la stringa
    parole = s.split() # ['ciao','ciao','bello','mio','mio.']
    parole_distinte = set(parole) # {'ciao','bello','mio','mio.'}
    res.append(len(parole_distinte))
    # terzo = len(parole_distinte)
    # quante frasi ha la stringa
    res.append(len(s.split('.')) - 1)
    # quarto = len(s.count('.'))
    # res[-1] = s.count('.')
    # s = "ciao bello. come stai."
    # s.split('.') -> ['ciao bello', 'come stai', '']
    # return [primo, secondo, terzo, quarto]
    return res

print(counter(s))