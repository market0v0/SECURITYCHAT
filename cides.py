




def Ceasar(code,key):
    result = ""
    for i in range(len(code)):
        char = code[i]
        if (char.isupper()):
            result += chr((ord(char) + key-65) % 26 + 65)
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
 
    return result
