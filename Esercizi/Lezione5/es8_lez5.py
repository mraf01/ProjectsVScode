def word_count(s: str) -> dict[str, int]:
    """
    Questa funzione conta l'occorrenza delle parole di una stringa.

    Esempio: se la stringa è "ciao come stai, tutto bene. ciao io sto bene", 
    filtrando le parole che compaiono più di una volta
    il risultato deve essere:
    {'ciao': 2, 'bene': 2}
    """
    # Rimuovi i segni di punteggiatura dalla stringa
    s = s.replace('.', '').replace(',', '').replace(';', '').replace('!', '').replace('?','')

    # Dividi la stringa in parole
    words = s.split()

    # Conta le occorrenze di ciascuna parola
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Filtra le parole che compaiono più di una volta
    filtered_counts = {word: count for word, count in word_counts.items() if count > 1}

    return filtered_counts

# Esempio di utilizzo
test_string: str = "ciao come stai, tutto bene. ciao io sto bene"
result: dict[str, int] = word_count(test_string)
print(result)