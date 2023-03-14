
def Ceasar(code,key):
    result = ''
    for i in range(len(code)):
        char = code[i]
        if (char.isupper()):
            result += chr((ord(char) + key-65) % 26 + 65)
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
    return result

def Polyalphabetic(plaintext, key, todo):
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():

            shift = ord(key[key_index].lower()) - 97
            cipher_char = chr(((ord(char.lower()) - 97 + (shift * todo)) % 26) + 97)
            ciphertext += cipher_char

            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += char
    return ciphertext

print(Polyalphabetic('mmrw','am',-1))
print(Ceasar('mark',3))