abc = [chr(i) for i in range(32, 127)]#алфавит
def encrypt(plaintext: str, shift: int):
    full_chipher = ''
    if shift > 0:#ставим нужный знак шагу
        shift_original = shift % 95
    else:
        shift_original = -(abs(shift) % 95)
    for el in plaintext:
        if 32 <= ord(el) + shift_original <= 126:
            full_chipher += chr(ord(el) + shift_original)
        else:
            if shift_original > 0:#если выходим за "границу алфавита"
                id = abs(126 - (ord(el) + shift_original))
                full_chipher += abc[id-1]
            if shift_original < 0:#тоже самое только с другой стороны
                id = (93 - (30 - (ord(el) + shift_original)))
                full_chipher += abc[id]
    return full_chipher
def decrypt(ciphertext: str, shift: int):
    return encrypt(ciphertext, -shift)#для расшифрровки нужно сделать отцительный шаг