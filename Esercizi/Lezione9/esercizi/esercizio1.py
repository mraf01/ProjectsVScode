'''
Data una stringa s e una lista di stringhe wordDict, restituisce True se s può essere segmentato in 
una sequenza separata da spazi di una o più parole del dizionario; False altrimenti.

Tieni presente che la stessa parola nel dizionario può essere riutilizzata più volte nella segmentazione.
'''

def word_break(s: str, wordDict: list[str]) -> bool:
    insieme_parole = set(wordDict)
    coda = [0]
    
    visitati = set()
    visitati.add(0)
    
    while coda:
        inizio = coda.pop(0)
        for fine in range(inizio + 1, len(s) + 1):
            if s[inizio:fine] in insieme_parole:
                if fine == len(s):
                    return True
                if fine not in visitati:
                    coda.append(fine)
                    visitati.add(fine)
    return False


# Test
print(word_break("leetcode", ["leet", "code"]))  # True
print(word_break("applepenapple", ["apple", "pen"]))  # True
print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # False



# metodo con programmazione dinamica
# def word_break(s: str, wordDict: list[str]) -> bool:
#     d = [False] * (len(s) + 1)  
#     d[0] = True
#     for i in range(1, len(s) + 1):
#         for j in range(i):
#             if d[j] and s[j:i] in wordDict:
#                 d[i] = True
#                 break
#     return d[-1]