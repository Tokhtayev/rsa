def generate_key(string, key):
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def vigenere_encrypt(string, key):
    cipher_text = []
    key = generate_key(string, key)
    for i in range(len(string)):
        if string[i].isalpha():
            offset = 65 if string[i].isupper() else 97
            x = (ord(string[i]) + ord(key[i].upper()) - 2 * offset) % 26
            x += offset
            cipher_text.append(chr(int(x)))
        else:
            cipher_text.append(string[i])
    return "".join(cipher_text)

def vigenere_decrypt(cipher_text, key):
    orig_text = []
    key = generate_key(cipher_text, key)
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            offset = 65 if cipher_text[i].isupper() else 97
            x = (ord(cipher_text[i]) - ord(key[i].upper()) + 26) % 26
            x += offset
            orig_text.append(chr(int(x)))
        else:
            orig_text.append(cipher_text[i])
    return "".join(orig_text)
