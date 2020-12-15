"""модуль для роботи з файлами даниих
- зчитування та вивід на екран
"""


def get_dovidnyk():
    """ Повертає дані довідника, які отримує з файлу "dovidnyk.txt"
    Returns:
        dani_dovidnyka: дані довідника
    """

    
    with open("I:/project/ICS-6-Shevchenko/ICS-6-Shevchenko/data/dovidnyk.txt", encoding="utf-8") as dovidnyk_file:
        from_file = dovidnyk_file.readlines()

    # накопичувач клієнтів
    dani_dovidnyka = []

    for line in from_file: 
        #відрізати '\n' в кінці рядка
        line = line[:-1]
        line_list = line.split(';')
        dani_dovidnyka.append(line_list)

    
    return dani_dovidnyka

def show_dovidnyk(dovidnyk):
    """ Виводить на екран довідник показників підприємства за заданим кодом
    Args:
        dovidnyk ([list]): довідник
    """
  
    

    kol_lines = 0
    
    for nazva_pokaznyka in dovidnyk:
            print("Код підприємства: {:2}; Назва підприємства: {:2}; Площа торгового залу: {:2};".format(nazva_pokaznyka[0], nazva_pokaznyka[1], nazva_pokaznyka[2]))
            kol_lines += 1

   

#dovidnyk = get_dovidnyk()   
# show_dovidnyk(dovidnyk)



def get_osnovni_pokaznyky():
    """ Повертає дані основних показнкиів, який отримує з "osnovni_pokaznyky.txt"
    Returns:
        dani_osnovnyh_pokaznykiv: дані основних показників
    """

    
    with open("I:/project/ICS-6-Shevchenko/ICS-6-Shevchenko/data/osnovni_pokaznyky.txt", encoding="utf-8") as pokaznyky_file:
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
    """ Виводить на екран список основних показників діяльності підприємства по заданому коду
    Args:
        osnovni_pokaznyky ([list]): основні показники
    """
  
    

    kol_lines = 0

    for pokaznyk in osnovni_pokaznyky:
            print("Код підприємства: {:2}; Період: {:2}; Роздрібний товарообіг: {:2}; Валовий доход: {:2}; Витрати обігу: {:2}; Прибуток від реальзації: {:2}; Прибуток від іншої реалізації: {:2}; Податок на прибуток: {:2}; ".format(pokaznyk[0], pokaznyk[1], pokaznyk[2], pokaznyk[3], pokaznyk[4], pokaznyk[5], pokaznyk[6], pokaznyk[7],))
            kol_lines += 1
   

#osnovni_pokaznyky = get_osnovni_pokaznyky()   
# show_osnovni_pokaznyky(osnovni_pokaznyky)
