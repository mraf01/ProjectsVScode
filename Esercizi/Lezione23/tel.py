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