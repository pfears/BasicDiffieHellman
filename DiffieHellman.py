'''
Simple python script that shows the most basic usage of the Diffie-Hellman Encryption
'''

from random import randint

class Person(): #Object used to define the encrypted Interaction
    def __init__(self,g,m):
        self.x = randint(1,99999) #secret key
        self.g = g #Public Base
        self.m = m #Public Modulas
    def createKey(self):
        temp = self.g**self.x
        temp = temp % self.m
        return temp
    def calculate(self, y):
        temp = y**self.x
        temp = temp % self.m
        return temp


    '''
    1) Initiating computer establishes the public base and modulas
    2) Add in support for basic puncuation
    '''
def encrypt(x, msg): #encrypts clear text to numeric cypher
    letters = {'a': 1, 'b': 2, 'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,
               'm':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,
               'y':25,'z':26}
    newLetters = letters
    for letter in newLetters:
        newLetters[letter]+= x
        newLetters[letter]%= 26
    msg=msg.lower()
    enc =''
    for char in range(len(msg)):
        x = msg[char]
        x = newLetters.get(x)
        if x is None:
            x = '27' #27 replaces a space inbetween words, could make this a calculated value
        enc = f'{enc}{x} '
    return enc

def decrypt(z, enc): #Decrypts cipher back to normal alphabet (Step 1 in decryption process)
    dec = ''
    x = [int(i) for i in enc.split() if i.isdigit()] #list comprehension that takes integers from strings and places them into a list
    for c in range(len(x)):
        if x[c] == 27: #ignores modification to 27 because that is listed a space
            x[c] = 27    
        else:
            x[c]=(x[c]-z)%26
        dec = f'{dec}{x[c]} '
    return dec
def clearText(dec):
    decMsg = ''
    finalKey={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',
              16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z',27:' '}
    x = [int(i) for i in dec.split() if i.isdigit()] #list comprehension that takes integers from strings and places them into a list
    for c in range(len(x)):
        x[c] = finalKey.get(x[c])
        decMsg = f'{decMsg}{x[c]}'
    return decMsg



g = randint(1,999999) #Establish Public Base
m = randint(1,999999) #Establish Public Modulas
bob = Person(g,m)
alice = Person(g,m)

x = bob.createKey() # Create Partial key to send to Alice
y = alice.createKey() # Create Partial key to send to Bob
z = bob.calculate(y) #Complete Key calculation to establish usable encryption
c = alice.calculate(x) #Complete Key calculation to establish usable encryption

enc = encrypt(z,"hi there")
enc2 = encrypt(c,"Hello How are you doing today")

print(f'Encryped Message from Bob: {enc}')
dec = decrypt(z,enc)
print(f'Decrypted Message from Bob: {dec}')
final = clearText(dec)
print(f'Clear Text Message from Bob: {final}')

print(f'Encryped Message from Alice: {enc2}')
dec2 = decrypt(c,enc2)
print(f'Decrypted Message from Alice: {dec2}')
final2 = clearText(dec2)
print(f'Clear Text Message from Alice: {final2}')




