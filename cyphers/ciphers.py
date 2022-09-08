# ----------------------Index Sub Cipher----------------------
def encryptIndexSubstitutionCipher(text):
    t = ''
    for x in range(0, len(text)):
        j = ord(text[x]) - 96
        if j < 10:
            t += '0' + str(j) + ' '
        else:
            t += str(j) + ' '
    return t

def decryptIndexSubstitutionCipher(text):
    t = ''
    for x in range(0, len(text), 3):
        t += chr(int(text[x]) * 10 + int(text[x + 1]) - 1 + ord('a'))
    return t
# ----------------------Morse Code----------------------
morseCode = {
    'a': '._',
    'b': '_...',
    'c': '_._.',
    'd': '_..',
    'e': '.',
    'f': '.._.',
    'g': '__.',
    'h': '....',
    'i': '..',
    'j': '.___',
    'k': '_._',
    'l': '._..',
    'm': '__',
    'n': '_.',
    'o': '___',
    'p': '.__.',
    'q': '__._',
    'r': '._.',
    's': '...',
    't': '_',
    'u': '.._',
    'v': '..._',
    'w': '.__',
    'x': '_.._',
    'y': '_.__',
    'z': '__..'
}

def encryptMorseCode(text):
    t = ''
    for x in range(0, len(text)):
        j = (morseCode.get(text[x]))
        t += str(j) + ' '
    return t

def decryptMorseCode(text):
    text += ' '
    t = ''
    temp = ''
    for x in text:
        if (x != ' '):
            i = 0
            temp += x
        else:
            i += 1
            if i == 2:
                t += ' '
            else:
                t += list(morseCode.keys())[list(morseCode.values()).index(temp)]
                temp = ''
    return t
# ----------------------Affine Cipher----------------------
def encryptAffineCipher(text, a, b):
    t = ''
    for x in text:
        t += chr((a * (ord(x) - 97) + b) % 26 + 97)
    return t

def decryptAffineCipher(text, a, b):
    t = ''
    for x in text:
        t += chr((pow(a, -1, 26) * ((ord(x) - 97) - b) % 26) + 97)
    return t

# ----------------------Caesar Cipher----------------------
def encryptCaesarCipher(text, key1, key2):
    t = ''
    test = 0
    for x in range(0, len(text)):
        if x % 2 == 0:
            test = key1
        else:
            test = key2
        if chr(97) <= text[x] <= chr(122):
            t += chr((ord(text[x]) - 97 + test) % 26 + 97)
        elif chr(65) <= text[x] <= chr(90):
            t += chr((ord(text[x]) - 65 + test) % 26 + 65)
        elif chr(48) <= text[x] <= chr(57):
            t += chr((ord(text[x]) - 48 + test) % 10 + 48)
        else:
            t += text[x]
    return t


def decryptCaesarCipher(text, key1, key2):
    pass


# ----------------------Transposition Cipher----------------------
def encryptTranspositionCipher(text, key):
    pass

def decryptTranspositionCipher(text, key):
    pass

