def get_pokaznyky():
    with open("I:/project/ICS-6-Shevchenko/ICS-6-Shevchenko/data/new_pokaznyky.txt", encoding="utf-8") as newpokaznyky_file:
        from_file = newpokaznyky_file.readlines()

    dani_newpokaznyka = []    


    for line in from_file: 
        #відрізати '\n' в кінці рядка
        line = line[:-1]
        line_list = line.split(';')
        dani_newpokaznyka.append(line_list)


    return dani_newpokaznyka




def show_pokaznyky(pokaznyky):




    kol_lines = 0




    for nazva_pokaznika in pokaznyky:
            print("     {:2}               {:10}        {:2}           {:2}                   {:2}                   {:2}                  {:2}                  {:2} ".format(nazva_pokaznika[0], nazva_pokaznika[1], nazva_pokaznika[2], nazva_pokaznika[3], nazva_pokaznika[4], nazva_pokaznika[5], nazva_pokaznika[6], nazva_pokaznika[7]))
            kol_lines += 1

#pokaznyky = get_pokaznyky()
#show_pokaznyky(pokaznyky)
