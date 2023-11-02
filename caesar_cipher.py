"""
-------------
caesar cipher
-------------
In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher,
Caesar's code, or Caesar shift, is one of the simplest and most widely known encryption techniques.
It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.
The method is named after Julius Caesar, who used it in his private correspondence. 

wikipedia
"""


import string


def encrypt(text: str, key: int) -> str:
    """
    -------
    encrypt
    -------
    Encode a given text with Caesar cipher and return the cipher-text.
    """


    result = str()
    for char in text:
        
        if char in string.ascii_lowercase:
            result += string.ascii_lowercase[(string.ascii_lowercase.index(char) + key) % 26]
        
        elif char in string.ascii_uppercase:
            result += string.ascii_uppercase[(string.ascii_uppercase.index(char) + key) % 26]
        
        elif char in string.digits:
            result += string.digits[(string.digits.index(char) + key) % 10]
        
        else:
            result += char
    
    return result



def decrypt(text: str, key: int) -> str:
    """
    -------
    decrypt
    -------
    Decode a cipher-text and return the plain-text.
    """

    
    result = str()
    for char in text:
        
        if char in string.ascii_lowercase:
            result += string.ascii_lowercase[(string.ascii_lowercase.index(char) - key) % 26]
        
        elif char in string.ascii_uppercase:
            result += string.ascii_uppercase[(string.ascii_uppercase.index(char) - key) % 26]
        
        elif char in string.digits:
            result += string.digits[(string.digits.index(char) - key) % 10]
        
        else:
            result += char
    
    return result
