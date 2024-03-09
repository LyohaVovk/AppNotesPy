# -*- coding: utf-8 -*-
from datetime import datetime
import json

def input_text():
    text = input("Введите текст заметки: \n")
    return text

def input_notes():
    # print("Здесь вводим заметку")
    
    command = '0'
    return command

def output_notes():
    # print("Здесь выводим существующую заметку")
    with open('Notes.json', 'r', encoding='utf-8') as f:
        notes_string = f.read()
        records = json.loads(notes_string)
        for key, value in records.items():
            print(f'UID: {key}')
            record = value
            for key, value in record.items():
                if key == 'title':
                    print(f'{value}')
                elif key == 'note':
                    print(f'    {value}')
                elif key == 'createDT':
                    print(f'                    Заметка создана: {value}')
                elif key == 'lastChangeDT':
                    print(f'                    Заметка изменена: {value}\n')    
            # print("")
    command = '0'
    return command

def edit_notes():
    print("Здесь редактируем заметку")
    command = '0'
    return command

def del_notes():
    print("Здесь удаляем заметку")
    command = '0'
    return command