alf = [chr(i) for i in range(32, 127)]
alf_lat = [chr(i) for i in range(65, 91)]
def encrypt(plaintext: str, keyword: str):
    full_key = ''
    keyword = keyword.upper()
    keyword_orig_bez_drugih_simvolov = ''
    for el in keyword:#очишаем кейвод от других символов
        if el in alf_lat:
            keyword_orig_bez_drugih_simvolov += el
        else:
            continue
    if len(keyword_orig_bez_drugih_simvolov) == 0:
        return ''
    for el in range(len(plaintext)):#цикл создает полный ключ для шифрования слова
        full_key += keyword_orig_bez_drugih_simvolov[el%len(keyword_orig_bez_drugih_simvolov)]
    shifr = ''
    for bukv in range(len(plaintext)):#наконец нас никто не сможет понять
        indx = alf.index(plaintext[bukv]) + alf_lat.index(full_key[bukv])
        shifr += alf[indx % 95]
    return shifr
print(encrypt('attack at dawn', 'LEMON'))
def decrypt(ciphertext: str, keyword: str):
    full_key = ''
    keyword = keyword.upper()
    keyword_orig_bez_drugih_simvolov = ''
    for el in keyword:
        if el in alf_lat:
            keyword_orig_bez_drugih_simvolov += el
        else:
            continue
    if len(keyword_orig_bez_drugih_simvolov) == 0:
        return ''
    for i in range(len(ciphertext)):
        full_key += keyword_orig_bez_drugih_simvolov[i%len(keyword_orig_bez_drugih_simvolov)]
    shifr = ''
    for bukv in range(len(ciphertext)):
        indx = alf.index(ciphertext[bukv]) - alf_lat.index(full_key[bukv])
        shifr += alf[indx % 95]
    return shifr
print(decrypt('lx!opv$m#-oe$|', 'LEMON'))
