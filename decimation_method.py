import string


def encrypt(text: str, key: int) -> str:
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits 
    result = str()
    
    for char in text:
        if char in lowercase:
            result += lowercase[(((lowercase.index(char)+1) * key) % 26) - 1]

        elif char in uppercase:
            result += uppercase[(((uppercase.index(char)+1) * key) % 26) - 1]

        elif char in numbers:
            result += numbers[(((numbers.index(char)+1) * key) % 10) - 1]
        
        else:
            result += char
    
    return result



def decrypt(text: str, key: int) -> str:
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits 
    result = str()

    for char in text:
        if char in lowercase:
            result += lowercase[(((lowercase.index(char)+1) // key) % 26) - 1]
    
    print(result)

# decrypt naghes