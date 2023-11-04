# try to decrypt decimation method cipher


from decimation_method import encrypt
import string

key = 3
cipher_text = "cfiloruxadgjmpsvybehknqtwz"


stringsList = list()
sid = 0
eid = len(cipher_text) // key
for i in range(key):
    stringsList.append(cipher_text[sid:eid])
    sid = eid
    eid += eid+1

result = str()
for c1, c2, c3 in zip(stringsList[0], stringsList[1], stringsList[2]):
    result += (c2+c3+c1)
result += (stringsList[1][-1] + stringsList[2][-1])
print(result == string.ascii_lowercase)