class Caesar():

    little_alpha = "abcdefghijklmnopqrstuvwxyz"
    big_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    
    def __init__(self, text, key=3):
        self.text = text
        self.key = key
        self.ciphertext = str()
        self.plaintext = str()

    def encipher(self):
        for i in self.text:
            if i in self.little_alpha:
                id = self.little_alpha.index(i)
                move = (id + self.key) % len(self.little_alpha)
                self.ciphertext += self.little_alpha[move]
            elif i in self.big_alpha:
                id = self.big_alpha.index(i)
                move = (id + self.key) % len(self.big_alpha)
                self.ciphertext += self.big_alpha[move]
            elif i in self.numbers:
                id = self.numbers.index(i)
                move = (id + self.key) % len(self.numbers)
                self.ciphertext += self.numbers[move]
            else:
                self.ciphertext += i
        

    def decipher(self):
        for i in self.text:
            if i in self.little_alpha:
                id = self.little_alpha.index(i)
                move = (id - self.key) % len(self.little_alpha)
                self.plaintext += self.little_alpha[move]
            elif i in self.big_alpha:
                id = self.big_alpha.index(i)
                move = (id - self.key) % len(self.big_alpha)
                self.plaintext += self.big_alpha[move]
            elif i in self.numbers:
                id = self.numbers.index(i)
                move = (id - self.key) % len(self.numbers)
                self.plaintext += self.numbers[move]
            else:
                self.plaintext += i
                