def is_palindrome(s: str) -> bool:

    """
        Restituisce True se s è palindroma; altrimenti restituisce False
        e.s. "Amo Roma" è una stringa palindroma
        e.s. "ciao come stai?" non è una stringa palindroma
    """
  
    s1: str = ""
    for i in range(len(s)-1, 0, -1):
        s1 += s[i]
        
    for i in range(len(s)):
        if s[i] != s1[i]:
            return False
    return True

string1: str = "Amo Roma"
string2: str = "ciao come stai?"
print(is_palindrome(string1))
print(is_palindrome(string2)
