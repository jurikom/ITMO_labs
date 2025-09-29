#границы алфавита
assci_start = 32
assci_end = 126
#размер алфавита
assci_range = 95

def hack(ciphertext):
    char_frequencies = {}#хранения частот
    for char in ciphertext:#заполняем счечик частот символами если уже есть символ то прибовляем 1 к его значению
        char_frequencies[char] = char_frequencies.get(char, 0) + 1
    
    most_char = ord(max(char_frequencies, key=char_frequencies.get))#находим код самого часто встречаемого символа
    shift = most_char - assci_start

    decrypted_text = ""
    for char in ciphertext:#используем шифр цезаря
        char_code = ord(char)

        shifted_code = char_code - shift - assci_start
        index = shifted_code % assci_range

        decrypted_char_code = index + assci_start

        decrypted_text += chr(decrypted_char_code)
    return decrypted_text
print(hack('uif!rvjdl!cspxo!gpy!kvnqt!pwfs!uif!mb{z!eph'))