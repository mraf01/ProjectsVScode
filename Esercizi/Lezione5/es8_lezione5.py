def word_count(s: str) -> dict[str, int]:
    """
    Questa funzione conta l'occorrenza delle parole di una stringa.

    Esempio: se la stringa è "ciao come stai, tutto bene. ciao io sto bene", 
    filtrando le parole che compaiono più di una volta
    il risultato deve essere:
    {'ciao': 2, 'bene': 2}
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
    # filtra soltanto le parole che compaiono < 1 volta
    d_filtered: dict[str, int] = dict()
    for key, val in d.items():
        if val > 1:
            d_filtered[key] = val
    return d_filtered


test_string: str = "ciao come stai, tutto bene. ciao io sto bene"
result: dict[str, int] = word_count(test_string)
print(result)