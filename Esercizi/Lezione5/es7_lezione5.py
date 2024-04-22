def word_count(s: str) -> dict[str, int]:
    """
        Questa funzione conta l'occorrenza delle parole
        di un stringa

        e.s.: se la stringa è "ciao come stai, tutto bene. ciao io sto bene"
        il risultato deve essere
        {"ciao": 2, "come": 1, "stai": 1, "tutto": 1, "bene": 2, "io": 1,"sto":1}
    """
    s: str = s.replace('.', '').replace(',','').replace(';','').replace('!','').replace('?', '')
    words: list[str] = s.split() # prendiamo le parole
    # devo vedere quante volte compaiono le parole in words
    # ["ciao", "come", "stai", "bene", "e", "tu", "come", "stai"]
    d: dict[str, int] = dict()
    for word in words: # scorriamo la lista words
        if word not in d:
            d[word] = 1
        else:
            d[word] = d[word] + 1
    return d


test_string: str = "ciao come stai, tutto bene. ciao io sto bene"
result: dict[str, int] = word_count(test_string)
print(result)