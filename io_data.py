# -*- coding: utf-8 -*-
from datetime import datetime
import json


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
            record = value
            for key, value in record.items():
                print(f'{key} = {value}')
        
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