# Шифрование текста
# 3 типа шифрования и дешифрования текста: ASCII, Цезарь, Морзе Рус/Англ
# Вызов функций происходит с помощью:
# from cryptotext import Cryptext
# obj = Cryptext('Ваш текст / Your text')
# obj."НАЗВАНИЕ ФУНКЦИИ"()

class Cryptext():
    ru_morse_dict = {
            'А': '•-', 'Б': '-•••', 'В': '•--', 'Г': '--•', 'Д': '-••', 'Е': '•',
            'Ж': '•••-', 'З': '--••', 'И': '••', 'Й': '•---', 'К': '-•-', 'Л': '•-••',
            'М': '--', 'Н': '-•', 'О': '---', 'П': '•--•', 'Р': '•-•','С': '•••',
            'Т': '-','У': '••-','Ф': '••-•','Х': '••••','Ц': '-•-•','Ч': '---•',
            'Ш': '----','Щ': '--•-','Ъ': '•--•-•','Ы': '-•--','Ь': '-••-','Э':
            '••-••','Ю': '••--','Я': '•-•-', ' ': '  ', '': ' ' }
    en_morse_dict = {
            'A': '•—', 'B': '—•••', 'C': '—•—•', 'D': '—••',
            'E': '•', 'F': '••—•', 'G': '——•', 'H': '••••',
            'I': '••', 'J': '•———', 'K': '—•—', 'L': '•—••',
            'M': '——', 'N': '—•', 'O': '———', 'P': '•——•',
            'Q': '——•—', 'R': '•—•', 'S': '•••', 'T': '—',
            'U': '••—', 'V': '•••—', 'W': '•——', 'X': '—••—',
            'Y': '—•——', 'Z': '——••', ' ': '  ', '': ' ' }


    def __init__(self,user_text,step_key):
        self.new_user_text = user_text.upper()
        self.user_text_list = list(self.new_user_text)
        self.step_key = step_key

    def ascii_crypt(self): #ASCII - шифрование текста по таблице кодов ASCII
        self.ascii_num = [ord(i) for i in self.user_text_list]
        #print(self.ascii_num)
        return self.ascii_num

    def ascii_descrypt(self): #ASCII - дешифрование текста по таблице кодов ASCII
        self.deascii_literal = [chr(i) for i in self.ascii_num]
        self.deascii_text = ''.join(self.deascii_literal)
        #print(self.deascii_text)
        return self.deascii_text

    def caesar_crypt(self): #Цезарь - шифрование методом Цезаря со сдвигом номера букву по кодировке ASCII на +step_key шагов
        self.step_key = int(self.step_key)
        self.caesar_num = [
            chr((ord(i) - 1040 + self.step_key) % 32 + 1040) if 1040 <= ord(i) <= 1071
            else chr((ord(i) - 65 + self.step_key) % 26 + 65) if 65 <= ord(i) <= 90
            else i  # Оставляем символ без изменений, если он не буква
            for i in self.user_text_list
        ]
        self.caesar_text = ''.join(self.caesar_num)
        #print(self.caesar_text)
        return self.caesar_text

    def caesar_descrypt(self): #Цезарь - дешифрование методом Цезаря со сдвигом номера букву по кодировке ASCII на +step_key шагов
        self.step_key = int(self.step_key)
        self.descaesar_literal = [
            chr((ord(i) - 1040 - self.step_key) % 32 + 1040) if 1040 <= ord(i) <= 1071
            else chr((ord(i) - 65 - self.step_key) % 26 + 65) if 65 <= ord(i) <= 90
            else i  # Оставляем символ без изменений, если он не буква
            for i in self.user_text_list
        ]
        self.descaesar_text = ''.join(self.descaesar_literal)
        #print(self.descaesar_text)
        return self.descaesar_text

    def morse_crypt_ru(self): #Морзе - шифрование методом Азбуки Морзе (Русский алфавит)
        self.morse_crypt = [Cryptext.ru_morse_dict[i] for i in self.user_text_list]
        self.morse_text = ' '.join(self.morse_crypt)
        #print(self.morse_text)
        return self.morse_text

    def morse_descrypt_ru(self): #Морзе - дешифрование методом Азбуки Морзе (Русский алфавит)
        self.morse_symbols = self.new_user_text.split('   ')
        self.demorse_crypt = [
            ''.join(key for symbol in word.split()
            for key, val in Cryptext.ru_morse_dict.items()
            if val == symbol) for word in self.morse_symbols
        ]
        self.demorse_text = ' '.join(self.demorse_crypt)
        #print(self.demorse_text)
        return self.demorse_text

    def morse_crypt_en(self): #Морзе - шифрование методом Азбуки Морзе (Английский алфавит)
        self.morse_crypt = [Cryptext.en_morse_dict[i] for i in self.user_text_list]
        self.morse_text = ' '.join(self.morse_crypt)
        #print(self.morse_text)
        return self.morse_text

    def morse_descrypt_en(self): #Морзе - дешифрование методом Азбуки Морзе (Английский алфавит)
        self.morse_symbols = self.new_user_text.split('   ')
        self.demorse_crypt = [
            ''.join(key for symbol in word.split()
            for key, val in Cryptext.en_morse_dict.items()
            if val == symbol) for word in self.morse_symbols
        ]
        self.demorse_text = ' '.join(self.demorse_crypt)
        #print(self.demorse_text)
        return self.demorse_text

    def vigenere_crypt_en(self): # Виженер - шифрование методом Виженера по ключевому слову
        self.step_key = str(self.step_key)
        self.step_key *= len(self.user_text_list) // len(self.step_key) + 1
        self.vigenere_cr_res = ''.join(
            [chr((ord(j) + ord(self.step_key[i])) % 26 + ord('A'))
             for i,j in enumerate(self.user_text_list)])
        #print(vigenere_cr_res)
        return self.vigenere_cr_res


    def vigenere_descrypt_en(self): # Виженер - дешифрование методом Виженера по ключевому слову
        self.step_key = str(self.step_key)
        self.step_key *= len(self.user_text_list) // len(self.step_key) + 1
        self.vigenere_descr_res = ''.join(
            [chr((ord(j) - ord(self.step_key[i])) % 26 + ord('A'))
             for i, j in enumerate(self.user_text_list)])
        #print(vigenere_descr_res)
        return self.vigenere_descr_res

    def vigenere_crypt_ru(self): # Виженер - шифрование методом Виженера по ключевому слову
        self.step_key = str(self.step_key)
        self.step_key *= len(self.user_text_list) // len(self.step_key) + 1
        self.vigenere_cr_res = ''.join(
            [chr((ord(j) + ord(self.step_key[i])) % 32 + ord('А'))
             for i,j in enumerate(self.user_text_list)])
        #print(vigenere_cr_res)
        return self.vigenere_cr_res


    def vigenere_descrypt_ru(self): # Виженер - дешифрование методом Виженера по ключевому слову
        self.step_key = str(self.step_key)
        self.step_key *= len(self.user_text_list) // len(self.step_key) + 1
        self.vigenere_descr_res = ''.join(
            [chr((ord(j) - ord(self.step_key[i])) % 32 + ord('А'))
             for i, j in enumerate(self.user_text_list)])
        #print(vigenere_descr_res)
        return self.vigenere_descr_res



#user_input = input('Введите текст, который необходимо зашифровать:')
#user_text = Cryptext(user_input)
#user_text.ascii_crypt()
#ser_text.ascii_descrypt()
#step_key = int(input('Введите размер шага:'))
#user_text.caesar_crypt(step_key)
#user_text.caesar_descrypt(step_key)
