# -*- coding: utf-8 -*-
from datetime import datetime
import json
import template as tp

def read_dict_from_file():
    """Чтение объекта json из файла в словарь"""
    with open('Notes.json', 'r', encoding='utf-8') as f:
        notes_string = f.read()
        records = json.loads(notes_string)
        
    return records

def write_dict_to_file(new_dict):
    with open('Notes.json', 'w', encoding='utf-8') as f:
        json.dump(new_dict, f)

def input_title():
    title = input("Введите заголовок заметки: \n")
    return title

def input_text():
    text = input("Введите текст заметки: \n")
    return text

def get_DT():
    curr_dt = datetime.now().isoformat(sep=' ')
    return curr_dt

def get_next_UID(notes_dict):
    uid_list = []
    for key in notes_dict.keys():  
        uid_list.append(key)
    
    next_uid = int(uid_list[-1]) + 1
    return next_uid

def input_notes():
    tp.records_template['title'] = input_title()
    tp.records_template['note'] = input_text()
    records = read_dict_from_file()        
    new_UID = get_next_UID(records)
    tp.records_template['createDT'] = get_DT()                 
    records[new_UID] = tp.records_template    
    write_dict_to_file(records)    
    command = '0'
    return command

def output_notes():
    # print("Здесь выводим существующую заметку")
    records = read_dict_from_file()
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