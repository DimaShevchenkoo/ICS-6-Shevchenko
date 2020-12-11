"""модуль для роботи з файлами даниих
- зчитування та вивід на екран
"""


def get_dovidnyk():
    """ Повертає дані довідника, які отримує з файлу "dovidnyk.txt"
    Returns:
        dani_dovidnyka: дані довідника
    """

    
    with open("./data/dovidnyk.txt", encoding="utf-8") as dovidnyk_file:
        from_file = dovidnyk_file.readlines()

    
    dani_dovidnyka = []

    for line in from_file: 
        #відрізати '\n' в кінці рядка
        line = line[:-1]
        line_list = line.split(';')
        dani_dovidnyka.append(line_list)

    
    return dani_dovidnyka

def show_dovidnyk(dovidnyk):
    """ Виводить на екран список довідник показників підприємства за заданим кодом
    Args:
        dovidnyk ([list]): довідник
    """
  
    nazva_pokaznyka_code = input("Введіть код довідника: ")

    kol_lines = 0
    
    for nazva_pokaznyka in dovidnyk:
        if nazva_pokaznyka_code == nazva_pokaznyka[0]:
            print("Код підприємства: {:4}; Назва підприємства: {:25}; площа торгового залу: {:5};".format(nazva_pokaznyka[0], nazva_pokaznyka[1], nazva_pokaznyka[2]))
            kol_lines += 1

    if kol_lines == 0:
        print("Не існує")

#dovidnyk = get_dovidnyk()   
# show_dovidnyk(dovidnyk)



def get_osnovni_pokaznyky():
    """ Повертає дані основних показнкиів, який отримує з "osnovni_pokaznyky.txt"
    Returns:
        dani_osnovnyh_pokaznykiv: дані основних показників
    """

    
    with open("./data/osnovni_pokaznyky.txt", encoding="utf-8") as pokaznyky_file:
        from_file = pokaznyky_file.readlines()

    # накопичувач клієнтів
    dani_osnovnyh_pokaznykiv = []

    for line in from_file: 
        #відрізати '\n' в кінці рядка
        line = line[:-1]
        line_list = line.split(';')
        dani_osnovnyh_pokaznykiv.append(line_list)

    
    return dani_osnovnyh_pokaznykiv

def show_osnovni_pokaznyky(osnovni_pokaznyky):
    """ Виводить на екран список основних показників 
    Args:
        osnovni_pokaznyky ([list]): основні показники
    """
  
    pokaznyk_code = input("Введіть код показника: ")

    kol_lines = 0

    for pokaznyk in osnovni_pokaznyky:
        if pokaznyk_code == pokaznyk[1]:
            print("Код підприємства: {:14}; Період: {:4}; Роздрібний товарообіг: {:11}; Валовий доход: {:11}; Витрати обігу: {}; Прибуток від реальзації: {}; Прибуток від іншої реалізації: {}; Податок на прибуток: {}; ".format(pokaznyk[0], pokaznyk[1], pokaznyk[2], pokaznyk[3], pokaznyk[4], pokaznyk[5], pokaznyk[6], pokaznyk[7],))
            kol_lines += 1
    if kol_lines == 0:
        print("Не існує")

#osnovni_pokaznyky = get_osnovni_pokaznyky()   
# show_osnovni_pokaznyky(osnovni_pokaznyky)
