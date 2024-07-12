'''
Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.

Un anagramma è una parola o una frase formata riorganizzando le lettere di una parola o frase diversa, 
in genere utilizzando tutte le lettere originali esattamente una volta.
'''

# soluzione efficiente
def anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count_s = {}
    count_t = {}

    for char in s.lower():
        if char in count_s:
            count_s[char] += 1
        else:
            count_s[char] = 1

    for char in t.lower():
        if char in count_t:
            count_t[char] += 1
        else:
            count_t[char] = 1

    return count_s == count_t


# soluzione inefficiente
# def anagram(s: str, t: str) -> bool:
#     return sorted(s.lower()) == sorted(t.lower())


# Test
print(anagram("anagram", "nagaram"))  # output: True
print(anagram("rat", "car"))  # output: False
print(anagram("silent", "listen"))  # output: True
print(anagram("NeurIPS", "UniReps"))  # output: True