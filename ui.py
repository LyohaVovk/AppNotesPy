# -*- coding: utf-8 -*-
from sys import exit
from interface import clear_screen, menu
from io_data import input_notes, output_notes, edit_notes, del_notes, find_notes

def main_screen():
    clear_screen()
    menu()
    command = input("Введите команду => ")
    while command != '6':
        
        while command != '' and command != '0' and command != '1' and command != '2' and command != '3' and command != '4' and command != '5':
            print("Введена неподдерживаемая команда! \n Попробуйте еще раз.")
            command = input("Введите команду => ")
        
        if command == '':
            clear_screen()
            menu()
            command = input("Введите команду => ")
            
        elif command == '0':
            command = input("Введите команду => ")
            
        elif command == '1':
            command = input_notes()
        elif command == '2':
            command = edit_notes()
        elif command == '3':
            command = output_notes()
        elif command == '4':
            command = find_notes()
        elif command == '5':
            command = del_notes()
        elif command == '6':
            exit(0)               