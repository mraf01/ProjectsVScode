'''
In questo problema ricreerete la classica gara tra la tartaruga e la lepre. Userete la generazione di numeri casuali 
per sviluppare una simulazione di questo memorabile evento. I contendenti iniziano la gara dal quadrato \#1 di un percorso 
composto da 70 quadrati. 
Ogni quadrato rappresenta una posizione lungo il percorso della corsa. Il traguardo è al quadrato 70 e il 
contendente che raggiunge per primo o supera questa posizione vince la gara. Durante la corsa, i contendenti 
possono occasionalmente perdere terreno. C'è un orologio che conta i secondi. Ad ogni tick dell'orologio, 
il vostro programma deve aggiornare la posizione degli animali secondo le seguenti regole:
- Tartaruga:
    - Passo veloce (50% di probabilità): avanza di 3 quadrati.
    - Scivolata (20% di probabilità): arretra di 6 quadrati. Non può andare sotto il quadrato 1.
    - Passo lento (30% di probabilità): avanza di 1 quadrato.
- Lepre:
    - Riposo (20% di probabilità): non si muove.
    - Grande balzo (20% di probabilità): avanza di 9 quadrati.
    - Grande scivolata (10% di probabilità): arretra di 12 quadrati. Non può andare sotto il quadrato 1.
    -  Piccolo balzo (30% di probabilità): avanza di 1 quadrato.
    - Piccola scivolata (20% di probabilità): arretra di 2 quadrati. Non può andare sotto il quadrato 1.
Il percorso è rappresentato attraverso l'uso di una lista. Usate delle variabili per tenere traccia delle posizioni 
degli animali (i numeri delle posizioni sono da 1 a 70). Fate partire ogni animale dalla posizione 1 (cioè ai "cancelli di partenza"). 
Se un animale scivola a sinistra prima del quadrato 1, riportatelo al quadrato 1.
Realizzate le percentuali delle mosse nell'elenco precedente generando un intero a caso, i, nell'intervallo 1 ≤ i ≤ 10. 
Per la tartaruga eseguite un "passo veloce" quando 1 ≤ i ≤ 5, una "scivolata" quando 6 ≤ i ≤ 7, o un "passo lento" quando 8 ≤ i ≤ 10. 
Usate una tecnica simile per muovere la lepre seguendo le sue regole.
Iniziate la gara stampando:
'BANG !!!!! AND THEY'RE OFF !!!!!'
Quindi, per ogni tick dell'orologio (ossia per ogni iterazione di un ciclo), stampate una lista di 70 posizioni che mostra 
la lettera 'T' nella posizione della tartaruga, la lettera 'H' nella posizione della lepre, il carattere '_' nelle posizioni libere. 
Occasionalmente, i contendenti si troveranno sullo stesso quadrato. In questo caso la tartaruga morde la lepre e il vostro 
programma deve stampare 'OUCH!!!' iniziando da quella posizione. 
Tutte le posizioni di stampa diverse dalla 'T', dalla 'H' o dal 'OUCH!!!' (in caso della stessa posizione) devono essere il carattere '_'.
Dopo la stampa di ogni tick, verificate se gli animali hanno raggiunto o superato il quadrato 70. 
Se è così, stampate il nome del vincitore e terminate la simulazione. Se vince la tartaruga, stampate "TORTOISE WINS! || VAY!!!". 
Se vince la lepre, stampate "HARE WINS || YUCH!!!". Se allo stesso tick dell'orologio vincono tutti e due gli animali, 
potreste voler favorire la tartaruga (la "sfavorita"), oppure stampare "IT'S A TIE.". Se non vince nessun animale, eseguite una nuova 
iterazione per simulare il successivo tick dell'orologio.
Requisiti del Codice:
- Utilizzare il modulo random per la generazione dei numeri casuali.
- Definire e utilizzare:
    - una funzione per visualizzare le posizioni sulla corsia di gara,
    - una funzione per calcolare la mossa della tartaruga,
    - una funzione per calcolare la mossa della lepre.
- Implementare un loop per simulare i tick dell'orologio. Ad ogni tick, calcolare le mosse, mostrare la posizione sulla corsia di gara, e 
determinare l'eventuale fine della gara.
 
SFIDE AGGIUNTIVE:
1. Variabilità Ambientale:
Introdurre fattori ambientali che possono influenzare la corsa, come il meteo.
Ad esempio, la pioggia può ridurre la velocità di avanzamento o aumentare la probabilità di scivolate per entrambi i concorrenti. 
Implementare un sistema dove le condizioni 'soleggiato' e 'pioggia' cambiano dinamicamente ogni 10 tick dell'orologio.
 
Modificatori mossa:
- La Tartaruga in caso di pioggia subisce penalità -1 su ogni mossa. In caso di sole non subisce variazioni.
- La Lepre in caso di pioggia subisca una penalità -2 su ogni mossa. In caso di sole non subisce variazioni.
 
2. Energia o Stamina:
Aggiungere una metrica di "energia" o "stamina" che diminuisce con ogni movimento e si ricarica in specifiche condizioni. 
Fare in modo che le mosse che consumano più energia non possano essere eseguite se l'animale non ha abbastanza energia. 
L'energia inziale per entrambi gli animali è 100.

Nuove regole di movimento:
- Tartaruga:
    - Per la tartaruga, ogni volta che il numero generato indica una mossa ma non è possibile eseguirla per mancanza di energia, 
    essa guadagna 10 di energia. Non può superare l'energia iniziale.
    - Passo veloce (50% di probabilità): avanza di 3 quadrati e richiede 5 di energia.
    - Scivolata (20% di probabilità): arretra di 6 quadrati e richiede 10 di energia. Non può andare sotto il quadrato 1.
    - Passo lento (30% di probabilità): avanza di 1 quadrato e richiede 3 di energia.

- Lepre:
    - Riposo (20% di probabilità): non si muove e recupera 10 di energia. Non può superare l'energia iniziale.
    - Grande balzo (20% di probabilità): avanza di 9 quadrati  e richiede 15 di energia.
    - Grande scivolata (10% di probabilità): arretra di 12 quadrati e richiede 20 di energia. Non può andare sotto il quadrato 1.
    - Piccolo balzo (30% di probabilità): avanza di 1 quadrato e richiede 5 di energia.
    - Piccola scivolata (20% di probabilità): arretra di 2 quadrati e richiede 8 di energia. Non può andare sotto il quadrato 1.
3. Ostacoli e Bonus
Sulla pista di gara sono presenti alcuni ostacoli e bonus a posizioni fisse, che influenzano direttamente il movimento degli animali 
quando vengono calpestati. Gli ostacoli causano uno slittamento all'indietro, mentre i bonus offrono un avanzamento extra.

Dettagli Implementativi:
- Ostacoli:
Posizionati a intervalli regolari sulla pista (es. ai quadrati 15, 30, 45), gli ostacoli riducono la posizione dell'animale di un numero 
specificato di quadrati (es: -3, -5, -7). Gli ostacoli sono rappresentati da un dizionario che mappa le posizioni degli ostacoli 
sul percorso (chiave) ed i relativi effetti (valore). Assicurarsi che nessun animale retroceda al di sotto del primo quadrato a seguito 
di un ostacolo.

- Bonus:
Dislocati strategicamente lungo la corsa (es. ai quadrati 10, 25, 50), i bonus aumentano la posizione dell'animale di 
un numero determinato di quadrati (es: 5, 3, 10). I bonus sono rappresentati da un dizionario che mappa le posizioni 
dei bonus sul percorso (chiave) ed i relativi effetti (valore). Consentire agli animali di beneficiare pienamente dei bonus, 
ma non oltrepassare il traguardo.
'''
import random

# con le sfide aggiuntive
def mossa_tartaruga(energia, meteo=0):
    i = random.randint(1, 10)
    if 1 <= i <= 5 and energia >= 5:
        energia -= 5
        return 3 - meteo, energia
    elif 6 <= i <= 7 and energia >= 10:
        energia -= 10
        return -6, energia
    elif 8 <= i <= 10 and energia >= 3:
        energia -= 3
        return 1 - meteo, energia
    else:
        energia = min(100, energia + 10)
        return 0, energia

def mossa_lepre(energia, meteo=0):
    i = random.randint(1, 10)
    if 1 <= i <= 2:
        energia = min(100, energia + 10)
        return 0, energia
    elif 3 <= i <= 4 and energia >= 15:
        energia -= 15
        return 9 - meteo, energia
    elif i == 5 and energia >= 20:
        energia -= 20
        return -12, energia
    elif 6 <= i <= 8 and energia >= 5:
        energia -= 5
        return 1 - meteo, energia
    elif 9 <= i <= 10 and energia >= 8:
        energia -= 8
        return -2, energia
    else:
        return 0, energia

def visualizza_corsia(tartaruga, lepre):
    for i in range(1, 71):
        if i == tartaruga == lepre:
            print('OUCH!!!', end='')
        elif i == tartaruga:
            print('T', end='')
        elif i == lepre:
            print('H', end='')
        else:
            print('_', end='')
    print()

def gara():
    tartaruga = lepre = 1
    energia_tartaruga = energia_lepre = 100
    meteo = 0
    ostacoli = {15: -3, 30: -5, 45: -7}
    bonus = {10: 5, 25: 3, 50: 10}
    print("BANG !!!!! AND THEY'RE OFF !!!!!")
    tick = 0
    while True:
        tick += 1
        if tick % 10 == 0:
            meteo = 1 if meteo == 0 else 0
        print(f'turno numero {tick}')
        mossa, energia_tartaruga = mossa_tartaruga(energia_tartaruga, meteo)
        tartaruga += mossa
        mossa, energia_lepre = mossa_lepre(energia_lepre, meteo)
        lepre += mossa
        tartaruga = max(1, tartaruga)
        lepre = max(1, lepre)
        if tartaruga in ostacoli:
            tartaruga = max(1, tartaruga + ostacoli[tartaruga])
        if lepre in ostacoli:
            lepre = max(1, lepre + ostacoli[lepre])
        if tartaruga in bonus:
            tartaruga = min(70, tartaruga + bonus[tartaruga])
        if lepre in bonus:
            lepre = min(70, lepre + bonus[lepre])
        visualizza_corsia(tartaruga, lepre)
        print()
        if tartaruga >= 70 and lepre >= 70:
            print("IT'S A TIE.")
            break
        elif tartaruga >= 70:
            print("TORTOISE WINS! || VAY!!!")
            break
        elif lepre >= 70:
            print("HARE WINS || YUCH!!!")
            break

gara()