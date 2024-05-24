'''
Given a string s which consists of lowercase or uppercase letters, write a function 
that returns the length of the longest palindrome that can be built with those letters. 
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

For example:

Test:
print(longest_palindrome("abccccdd"))    Result: 7
print(longest_palindrome("Aa"))          Result: 1
'''

def longest_palindrome(s: str) -> int:
    counts = set()
    for char in s:
        if char in counts:
            counts.remove(char)
        else:
            counts.add(char)
    # Sottraiamo 1 se ci sono caratteri dispari, quindi aggiungiamo 1 alla fine per contare il carattere dispari che può andare al centro
    return len(s) - len(counts) + min(1, len(counts))


# Test
print(longest_palindrome("abccccdd"))
print(longest_palindrome("Aa"))