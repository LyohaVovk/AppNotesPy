# -*- coding: utf-8 -*-
from sys import exit
from io_data import input_notes, output_notes, edit_notes, del_notes

def interface():
    print("Добро пожаловать в AppNotes")
    print("1. - Создать заметку;\n2. - Редактировать заметку;\n3. - Вывод заметок;\n4. - Удаление заметок;\n5. - Выход из программы")
    command = input("Введите команду: ")
    
    while command != '1' and command != '2' and command != '3' and command != '4' and command != '5':
        print("Введена неподдерживаемая команда! \n Попробуйте еще раз.")
        command = input("Введите команду: ")
        
    command = int(command)
    
    if command == 1:
        input_notes()
    elif command == 2:
        edit_notes()
    elif command == 3:
        output_notes()
    elif command == 4:
        del_notes()
    elif command == 5:
        exit(0)