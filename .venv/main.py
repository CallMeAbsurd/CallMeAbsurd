import tkinter as tk
from tkinter import font
from cryptotext import Cryptext  # Убедитесь, что этот файл существует и содержит класс Cryptext
import keyboard

class App:
    def __init__(self, root):
        self.root = root
        self.root.title('Шифратор/Дешифратор текста')
        self.root.geometry('600x700+200+200')

        # Создание жирного шрифта
        self.bold_font = font.Font(family='Helvetica', size=11, weight='bold')

        # Создание фрейма с фиксированными размерами
        self.frame_text = tk.Frame(self.root, bg='#dbd7d7', width=600, height=470)
        self.frame_text.pack_propagate(False)  # Запрещаем фрейму изменять свои размеры
        self.frame_text.pack(side=tk.TOP, fill=tk.X)

        # Создание текстовых меток и полей ввода
        self.create_widgets()

        # Создание фрейма для кнопок
        self.frame_btn = tk.Frame(self.root, bg='#242323', width=600, height=230)
        self.frame_btn.pack_propagate(False)  # Запрещаем фрейму изменять свои размеры
        self.frame_btn.pack(side=tk.TOP, fill=tk.X)

        # Создание кнопок и выпадающих списков
        self.create_buttons_and_menus()

        # Установка равного расстояния между колонками
        self.frame_btn.grid_columnconfigure(0, weight=1)
        self.frame_btn.grid_columnconfigure(1, weight=1)

        # Установка фиксированной высоты фрейма для кнопок
        self.frame_btn.config(height=200)

    def create_widgets(self):
        # Создание текстовых меток и полей ввода
        label1 = tk.Label(self.frame_text, text="Введите текст, который необходимо зашифровать:", bg='#dbd7d7',
                          font=self.bold_font)
        label1.pack(pady=5)

        self.input_text = tk.Text(self.frame_text, height=10, width=50)
        self.input_text.pack()

        label2 = tk.Label(self.frame_text, text='Введите ключ шифрования (если необходимо):', bg='#dbd7d7',
                          font=self.bold_font)
        label2.pack(pady=10)

        self.key_entry = tk.Entry(self.frame_text)
        self.key_entry.pack()

        # Кнопка "Копировать"
        copy_button = tk.Button(self.frame_text, text='Копировать в буфер обмена', command=self.copy_to_clipboard)
        copy_button.place(relx=0.1, rely=0.535, anchor='w')  # Размещаем кнопку слева от поля ввода

        # Кнопка "Вставить"
        paste_button = tk.Button(self.frame_text, text='Вставить из буфера обмена', command=self.paste_from_clipboard)
        paste_button.place(relx=0.9, rely=0.535, anchor='e')  # Размещаем кнопку справа от поля ввода

        label3 = tk.Label(self.frame_text, text='Результат:', bg='#dbd7d7', font=self.bold_font)
        label3.pack(pady=5)

        self.result_text = tk.Text(self.frame_text, height=10, width=50)
        self.result_text.pack()


    def create_buttons_and_menus(self):
        # Список методов шифрования и дешифрования
        self.encryption_methods = ['ASCII Шифрование', 'Шифрование Цезаря', 'Морзе Русский', 'Морзе Английский',
                              'Виженер Английский', 'Виженер Русский']
        self.descryption_methods = ['ASCII Дешифрование', 'Дешифрование Цезаря', 'Морзе Русский', 'Морзе Английский',
                               'Виженер Английский', 'Виженер Русский']

        # Переменные для хранения выбранных методов
        self.selected_method_encr = tk.StringVar(self.root)
        self.selected_method_encr.set(self.encryption_methods[0])  # Устанавливаем метод по умолчанию
        self.selected_method_descr = tk.StringVar(self.root)
        self.selected_method_descr.set(self.descryption_methods[0])  # Устанавливаем метод по умолчанию

        # Подписи для выпадающих списков
        label_btn1 = tk.Label(self.frame_btn, text='Методы шифрования:', fg='white', bg='#242323', font=self.bold_font)
        label_btn1.grid(row=0, column=0, padx=60, pady=5, sticky='w')

        label_btn2 = tk.Label(self.frame_btn, text='Методы дешифрования:', fg='white', bg='#242323',
                              font=self.bold_font)
        label_btn2.grid(row=0, column=1, padx=60, pady=5, sticky='w')

        # Создание выпадающего списка
        method_menu_encr = tk.OptionMenu(self.frame_btn, self.selected_method_encr, *self.encryption_methods)
        method_menu_encr.grid(row=1, column=0, padx=(20, 10), pady=5, sticky='ew')

        method_menu_descr = tk.OptionMenu(self.frame_btn, self.selected_method_descr, *self.descryption_methods)
        method_menu_descr.grid(row=1, column=1, padx=(10, 20), pady=5, sticky='ew')

        # Подпись для вставки символов
        label_insert = tk.Label(self.frame_btn, text='Вставить символы для Морзе:', fg='white', bg='#242323',
                                font=self.bold_font)
        label_insert.grid(row=2, column=0, columnspan=2, padx=170, pady=(5, 5), sticky='w')

        # Кнопки для вставки символов
        insert_dot_button = tk.Button(self.frame_btn, text='Вставить •',
                                      command=lambda: self.input_text.insert(tk.END, '•'))
        insert_dot_button.grid(row=3, column=0, padx=10, pady=(5, 10), sticky='ew')

        insert_dash_button = tk.Button(self.frame_btn, text='Вставить -',
                                       command=lambda: self.input_text.insert(tk.END, '-'))
        insert_dash_button.grid(row=3, column=1, padx=10, pady=(5, 10), sticky='ew')


        # Кнопка "Зашифровать"
        run_button_encr = tk.Button(self.frame_btn, text='Зашифровать', command=self.run_encryption)
        run_button_encr.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky='ew')

        # Кнопка "Дешифровать"
        run_button_descr = tk.Button(self.frame_btn, text='Дешифровать', command=self.run_descryption)
        run_button_descr.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

        # Привязываем сочетания клавиш для копирования и вставки
        #self.root.bind('<Control-C>', self.copy_to_clipboard)
        #self.root.bind('<Control-V>', self.paste_from_clipboard)
        keyboard.add_hotkey('ctrl+c',self.copy_to_clipboard)
        keyboard.add_hotkey('ctrl+v', self.paste_from_clipboard)
        keyboard.add_hotkey('ctrl+a', self.select_all)
    def select_all(self):
        try:
            # Получаем текущий фокус и выделяем текст в активном виджете
            current_widget = self.root.focus_get()
            if isinstance(current_widget, tk.Text):
                current_widget.tag_add('sel', '1.0', 'end')  # Выделяем весь текст
                current_widget.mark_set('insert', '1.0')  # Устанавливаем курсор в начало
                return 'break'  # Предотвращаем дальнейшую обработку события
            else:
                print("Текущий виджет не является текстовым виджетом.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def copy_to_clipboard(self, event=None):
        # Получаем выделенный текст из активного текстового поля
        try:
            current_widget = self.root.focus_get()  # Получаем текущее активное поле
            selected_text = current_widget.selection_get()  # Получаем выделенный текст
            self.root.clipboard_clear()  # Очищаем буфер обмена
            self.root.clipboard_append(selected_text)  # Добавляем текст в буфер обмена
        except tk.TclError:
            pass  # Игнорируем ошибку, если ничего не выделено

    def paste_from_clipboard(self, event=None):
        # Получаем текст из буфера обмена и вставляем его в активное текстовое поле
        try:
            current_widget = self.root.focus_get()  # Получаем текущее активное поле
            clipboard_text = self.root.clipboard_get()  # Получаем текст из буфера обмена

            if isinstance(current_widget, tk.Text):  # Проверяем, является ли текущий виджет текстовым
                # Удаляем выделенный текст
                try:
                    current_widget.delete("sel.first", "sel.last")  # Удаляем выделенный текст
                except tk.TclError:
                    pass  # Игнорируем ошибку, если ничего не выделено

                # Вставляем текст из буфера обмена
                current_widget.insert(tk.END, clipboard_text)  # Вставляем текст в активное поле
        except tk.TclError:
            pass  # Игнорируем ошибку, если буфер обмена пуст

    def run_encryption(self):
        # Получаем текст из поля ввода
        user_text = self.input_text.get("1.0", tk.END).strip()
        key_input = self.key_entry.get().strip()
        # Устанавливаем ключ в None, если ввод пустой
        key = key_input if key_input else None
        # Создаем экземпляр Cryptext с введенным текстом
        cryptext_instance = Cryptext(user_text,key)
        # Получаем выбранные методы
        selected_encryption_method = self.selected_method_encr.get()
        self.meth_id_enc = self.encryption_methods.index(selected_encryption_method)
        # Список функций шифрования
        encrypt_meth_list = [cryptext_instance.ascii_crypt,
        cryptext_instance.caesar_crypt,
        cryptext_instance.morse_crypt_ru,
        cryptext_instance.morse_crypt_en,
        cryptext_instance.vigenere_crypt_en,
        cryptext_instance.vigenere_crypt_ru]
        # Получаем функцию по индексу
        selected_encrypt_method = encrypt_meth_list[self.meth_id_enc]
        # Например, если нужно использовать метод шифрования:
        result = selected_encrypt_method()  # Пример вызова метода
        # Отображаем результат в поле результата
        self.result_text.delete("1.0", tk.END)  # Очищаем предыдущее содержимое
        self.result_text.insert(tk.END, result)  # Вставляем новый результат

    def run_descryption(self):
        # Получаем текст из поля ввода
        user_text = self.input_text.get("1.0", tk.END).strip()
        key_input = self.key_entry.get().strip()

        # Устанавливаем ключ в None, если ввод пустой
        key = key_input if key_input else None
        # Создаем экземпляр Cryptext с введенным текстом
        cryptext_instance = Cryptext(user_text, key)
        # Получаем выбранные методы
        selected_descryption_method = self.selected_method_descr.get()

        self.meth_id_enc = self.descryption_methods.index(selected_descryption_method)
        print(self.meth_id_enc)
        # Список функций шифрования
        descrypt_meth_list = [cryptext_instance.ascii_descrypt,
                             cryptext_instance.caesar_descrypt,
                             cryptext_instance.morse_descrypt_ru,
                             cryptext_instance.morse_descrypt_en,
                             cryptext_instance.vigenere_descrypt_en,
                             cryptext_instance.vigenere_descrypt_ru]
        # Получаем функцию по индексу
        selected_descrypt_method = descrypt_meth_list[self.meth_id_enc]
        # Здесь вы можете добавить логику для выбора метода шифрования или дешифрования
        # Например, если нужно использовать метод шифрования:
        result = selected_descrypt_method()  # Пример вызова метода

        # Отображаем результат в поле результата
        self.result_text.delete("1.0", tk.END)  # Очищаем предыдущее содержимое
        self.result_text.insert(tk.END, result)  # Вставляем новый результат

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()



