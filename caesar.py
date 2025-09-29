abc = [chr(i) for i in range(32, 127)]#алфавит
print(abc)
def encrypt(plaintext: str, shift: int):
    itog = ''
    if shift > 0:#ставим нужный знак большому шагу
        shag = shift % 95
    else:
        shag = -(abs(shift) % 95)
    for el in plaintext:
        if 32 <= ord(el) + shag <= 126:
            itog += chr(ord(el) + shag)
        else:
            if shag > 0:#если выходим за "границу алфавита"
                id = abs(126 - (ord(el) + shag))
                itog += abc[id-1]
            if shag < 0:#тоже самое только с другой стороны
                id = (93 - (30 - (ord(el) + shag)))
                itog += abc[id]
    return itog
def decrypt(ciphertext: str, shift: int):
    return encrypt(ciphertext, -shift)
print(encrypt("~", 1))
print(decrypt("Khoor/#Zruog$", 3))

