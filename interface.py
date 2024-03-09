# -*- coding: utf-8 -*-
""" Отрисовка меню и очистка экрана после вывода информации на экран """
import os

def menu():
    print("*******************************")
    print("* Добро пожаловать в AppNotes *")
    print("*******************************")
    print("*        Список команд        *")
    print("*******************************")
    print("*   1 - Создать заметку       *")
    print("*******************************")
    print("*   2 - Редактировать заметку *")
    print("*******************************")
    print("*   3 - Вывод заметок         *")
    print("*******************************")
    print("*   4 - Удаление заметок      *")
    print("*******************************")
    print("*   5 - Выход из программы    *")
    print("*******************************")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')