# -*- coding: utf-8 -*-
from sys import exit
from interface import clear_screen, menu
from io_data import input_notes, output_notes, edit_notes, del_notes

def main_screen():
    clear_screen()
    command = menu()
    while command != '5':
        
        while command != '1' and command != '2' and command != '3' and command != '4':
            print("Введена неподдерживаемая команда! \n Попробуйте еще раз.")
            command = input("Введите команду: ")
        
        if command == '1':
            input_notes()
        elif command == '2':
            edit_notes()
        elif command == '3':
            output_notes()
        elif command == '4':
            del_notes()
        elif command == '5':
            exit(0)               