"""головний модуль задачі
   - виводить на екран та в файл розрахункову таблицю
   - виводить на екран первинні файли
"""

import os
import data_service, process_data
from process_data import create_analiz
from data_service import show_dovidnyk, show_osnovni_pokaznyky, get_dovidnyk, get_osnovni_pokaznyky

MAIN_MENU = \
"""
~~~~~~~~~ ОБРОБКА ОСНОВНИХ ПОКАЗНИКІВ ~~~~~~~~~
1 - вивід показників на екран
2 - запис результату в файл
3 - вивід списку довідника
4 - вивід списку показників
0 - завершення роботи
------------------------------------------------
"""

TITLE = "АНАЛІЗ ОСНОВИХ ПОКАЗНИКІВ ПІДПРИЄМСТВА"

HEADER = \
"""
======================================================================================================================================================================
Назва підприємства       | Площа торгового залу | Період  | Роздрібний товарообіг, грн. | Рівень валового доходу | Балансовий прибуток, грн. | Чистий прибуток, грн. | 
======================================================================================================================================================================
"""

FOOTER = \
"""
======================================================================================================================================================================
"""

STOP_MESSAGE = "Для продовження натисніть <Enter>"

def show_analiz_table(index_list):
    """вивід на екран таблиці показників
    """
    print(f"\n\n{TITLE:^170}")
    print(HEADER)

    for index in index_list:
        print(f"{index['index_name']:24}",
              f"{index['area']:12}",
              f"{index['period']:14}",  
              f"{index['circulation']:>11}",
              f"{index['income']:>14}",
              f"{index['loss']:>13}",
              f"{index['profit']:>16.2f}",
              f"{index['clear profit']:>18.2f}"
              )
    print(FOOTER)

def write_analiz(index_list):
    """запис аналізу в файл
    """
    with open('./data/analiz.txt', "w") as analiz_file:
        for index in index_list:
            line = index['index_name'] + ';' + \
            str(index['area']) + ';' + \
            index['period'] + ';' + \
            str(index['circulation']) + ';' + \
            str(index['income']) + ';' + \
            str(index['loss']) + ';' + \
            str(index['profit']) + ';' + \
            str(index['clear profit']) + '\n'
            analiz_file.write(line)
    
    print("Файл успішно сформовано ...")     


while True:

    # очистити екран для Windows
    clear = lambda: os.system('cls')
    clear()

    # очистити екран для Linux i Mac
    clear = lambda: os.system('clear')

    print(MAIN_MENU)
    command_number = input("Введіть номер команди: ")

    # обробка команд користувача
    if command_number == '0':
        print('\nПрограма завершила роботу')
        exit(0)

    elif command_number == '1':
        index_list = create_analiz()
        show_analiz_table(index_list)
        input(STOP_MESSAGE)

    elif command_number == '2':
        index_list = create_analiz()
        write_analiz(index_list)
        input(STOP_MESSAGE)

    elif command_number == '3':
        dovidnyk = get_dovidnyk()
        show_dovidnyk(dovidnyk)
        input(STOP_MESSAGE)

    elif command_number == '4':
        osnovni_pokaznyky = get_osnovni_pokaznyky()
        show_osnovni_pokaznyky(osnovni_pokaznyky)
        input(STOP_MESSAGE)   