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
    """Запись объекта json а файл"""
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

def get_UID(notes_dict):
    pass

def get_next_UID(notes_dict):
    uid_list = []
    for key in notes_dict.keys():  
        uid_list.append(key)
    
    next_uid = int(uid_list[-1]) + 1
    return next_uid

def input_UID():
    UID = input("Введите идентификатор заметки: \n")
    return UID

def input_notes():
    """Функция ввода заметок"""
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
    """Функция вывода заметок"""
    records = read_dict_from_file()
    variants = input("Введите идентификатор заметки для вывода или нажмите Enter для вывода всех заметок: ")
    if variants == "":
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
    else:
        if variants in records.keys():
            print(f'UID: {variants}')
            record = records[variants]
            for key, value in record.items():
                if key == 'title':
                    print(f'{value}')
                elif key == 'note':
                    print(f'    {value}')
                elif key == 'createDT':
                    print(f'                    Заметка создана: {value}')
                elif key == 'lastChangeDT':
                    print(f'                    Заметка изменена: {value}\n')
        else:
            print("Нет такого идентификатора!")
            
    command = '0'
    return command

def find_notes():
    """Функция поиска заметок по времени или идентификатору"""
    start_DT = input("Введите дату, с которой надо начать поиск заметок(в формате ГГГГ-ММ-ДД ЧЧ:ММ:СС): ")
    stop_DT = input("Введите дату, до которой нужно искать заметки(в формате ГГГГ-ММ-ДД ЧЧ:ММ:СС): ")
    start_date = datetime.strptime(start_DT, '%Y-%m-%d %H:%M:%S')
    stop_date = datetime.strptime(stop_DT, '%Y-%m-%d %H:%M:%S')
    records = read_dict_from_file()
    for key, value in records.items():
        record = value
        note_time = datetime.strptime(record["createDT"], '%Y-%m-%d %H:%M:%S.%f')
        if note_time > start_date and note_time < stop_date:
            print(f'UID: {key}')
            for key, value in record.items():
                if key == 'title':
                    print(f'{value}')
                elif key == 'note':
                    print(f'    {value}')
                elif key == 'createDT':
                    print(f'                    Заметка создана: {value}')
                elif key == 'lastChangeDT':
                    print(f'                    Заметка изменена: {value}\n')
        else:
            print("Заметки в это время не содавались!")
             
    command = '0'
    return command

def edit_notes():
    """Функция редактирования заметок"""
    records = read_dict_from_file()
    UID = input_UID()
    record = records[UID]
    record['note'] = input_text()
    record['lastChangeDT'] = get_DT()
    
    records[UID] = record    
    write_dict_to_file(records)
    command = '0'
    return command

def del_notes():
    """Функция удаления заметок"""
    records = read_dict_from_file()
    UID = input_UID()
    del records[UID]
    write_dict_to_file(records)
    command = '0'
    return command