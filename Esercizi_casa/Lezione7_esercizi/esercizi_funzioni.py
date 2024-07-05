def trova_chiave(dizionario, valore):
    for chiave, val in dizionario.items():
        if val == valore:
            return chiave
    return None

def inverti_dizionario(dizionario):
    return {valore: chiave for chiave, valore in dizionario.items()}

def filtra_e_moltiplica(lista, fattore):
    return [num * fattore for num in lista if num % 2 == 0]

def is_magico(numero):
    return numero % 4 == 0 and numero % 6 != 0

def somma_divisibili(lista):
    return sum(num for num in lista if num % 2 == 0 and num % 3 == 0)

def filtra_e_sconta_prodotti(prodotti):
    return {prodotto: prezzo * 0.9 for prodotto, prezzo in prodotti.items() if prezzo > 20}

def aggrega_voti(lista_voti):
    voti_aggregati = {}
    for record in lista_voti:
        studente = record['studente']
        voto = record['voto']
        if studente in voti_aggregati:
            voti_aggregati[studente].append(voto)
        else:
            voti_aggregati[studente] = [voto]
    return voti_aggregati

def rimuovi_elementi(lista, elementi_da_rimuovere):
    for elemento, conteggio in elementi_da_rimuovere.items():
        for _ in range(conteggio):
            if elemento in lista:
                lista.remove(elemento)
    return lista

def converti_in_dizionario(lista_tuple):
    dizionario = {}
    for chiave, valore in lista_tuple:
        if chiave in dizionario:
            dizionario[chiave].append(valore)
        else:
            dizionario[chiave] = [valore]
    return dizionario

def classifica_pari_dispari(lista):
    classificazione = {'pari': [], 'dispari': []}
    for numero in lista:
        if numero % 2 == 0:
            classificazione['pari'].append(numero)
        else:
            classificazione['dispari'].append(numero)
    return classificazione

def converti_temperatura(valore, scala='C'):
    if scala == 'C':
        return (valore * 9/5) + 32
    elif scala == 'F':
        return (valore - 32) * 5/9
    else:
        raise ValueError("Scala non valida. Usa 'C' per Celsius o 'F' per Fahrenheit.")

def somma_maggiori_di(lista, soglia):
    return sum(num for num in lista if num > soglia)

def frequenza_elementi(lista):
    frequenze = {}
    for elemento in lista:
        if elemento in frequenze:
            frequenze[elemento] += 1
        else:
            frequenze[elemento] = 1
    return frequenze

def unisci_dizionari(diz1, diz2):
    diz_unito = diz1.copy()
    for chiave, valore in diz2.items():
        if chiave in diz_unito:
            diz_unito[chiave] += valore
        else:
            diz_unito[chiave] = valore
    return diz_unito

def rimuovi_da_insieme(insieme, lista_da_rimuovere):
    return insieme - set(lista_da_rimuovere)

def max_min_media(lista):
    if not lista:
        return None, None, None
    massimo = max(lista)
    minimo = min(lista)
    media = sum(lista) / len(lista)
    return massimo, minimo, media

def media_arrotondata(lista):
    if not lista:
        return None
    media = sum(lista) / len(lista)
    return round(media)

def rimuovi_duplicati(lista):
    vista = set()
    lista_senza_duplicati = []
    for elemento in lista:
        if elemento not in vista:
            lista_senza_duplicati.append(elemento)
            vista.add(elemento)
    return lista_senza_duplicati

def ruota_sinistra(lista, k):
    k = k % len(lista)
    return lista[k:] + lista[:k]

def controllo_accesso(username, password, attivo):
    return username == "admin" and password == "12345" and attivo

def verifica_condizioni(A, B, C):
    return A or (B and C)

def conto_alla_rovescia(numero):
    while numero >= 0:
        print(numero)
        numero -= 1

def contiene_7(numero):
    return '7' in str(numero)

def bilancia_parantesi(stringa):
    bilanciamento = 0
    for char in stringa:
        if char == '(':
            bilanciamento += 1
        elif char == ')':
            bilanciamento -= 1
        if bilanciamento < 0:
            return False
    return bilanciamento == 0

def conta_isolati(lista):
    isolati = 0
    lunghezza = len(lista)
    for i in range(lunghezza):
        if (i == 0 or lista[i] != lista[i-1]) and (i == lunghezza-1 or lista[i] != lista[i+1]):
            isolati += 1
    return isolati

def create_contact(nome_cognome, email=None, telefono=None):
    contatto = {'profile': nome_cognome}
    if email is not None:
        contatto['email'] = email
    if telefono is not None:
        contatto['telefono'] = telefono
    return contatto

def update_contact(contatto, nome_cognome, email=None, telefono=None):
    if contatto['profile'] == nome_cognome:
        if email is not None:
            contatto['email'] = email
        if telefono is not None:
            contatto['telefono'] = telefono
    return contatto

contatto = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=69876543)
print(contatto)
contatto_aggiornato = update_contact(contatto, "Mario Rossi", telefono=123456789)
print(contatto_aggiornato)