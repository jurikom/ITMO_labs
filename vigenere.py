alf = [chr(i) for i in range(32, 127)]
alf_lat = [chr(i) for i in range(65, 91)]
def encrypt(plaintext: str, keyword: str):
    full_key = ''
    keyword = keyword.upper()
    keyword_original = ''
    for el in keyword:#очишаем кейвод от других символов
        if el in alf_lat:
            keyword_original += el
        else:
            continue
    if len(keyword_original) == 0:
        return ''
    for el in range(len(plaintext)):#цикл создает полный ключ для шифрования слова
        full_key += keyword_original[el%len(keyword_original)]
    chipher = ''
    for el in range(len(plaintext)):#наконец нас никто не сможет понять
        indx = alf.index(plaintext[el]) + alf_lat.index(full_key[el])
        chipher += alf[indx % 95]
    return chipher
print(encrypt('attack at dawn', 'LEMON'))
def decrypt(ciphertext: str, keyword: str):
    full_key = ''
    keyword = keyword.upper()
    keyword_original = ''
    for el in keyword:
        if el in alf_lat:
            keyword_original += el
        else:
            continue
    if len(keyword_original) == 0:
        return ''
    for i in range(len(ciphertext)):
        full_key += keyword_original[i%len(keyword_original)]
    chipher = ''
    for el in range(len(ciphertext)):
        indx = alf.index(ciphertext[el]) - alf_lat.index(full_key[el])#это единственное отличие от шифровщика
        chipher += alf[indx % 95]
    return chipher
print(decrypt('lx!opv$m#-oe$|', 'LEMON'))
