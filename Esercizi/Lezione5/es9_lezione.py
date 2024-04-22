def is_palindrome(s: str) -> bool:

    """
        Restituisce True se s è palindroma; altrimenti restituisce False
        e.s. "Amo Roma" è una stringa palindroma
        e.s- "ciao come stai?" non è una stringa palindroma
    """
    s: str = s.lower().replace(' ', '')
    i: int = 0
    while i < len(s):
        j = len(s) - (i + 1)
        if s[i] != s[j]:
            return False
        i += 1
    return True

string1: str = "Amo Roma"
string2: str = "ciao come stai?"
print(is_palindrome(string1))
print(is_palindrome(string2))