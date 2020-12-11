""" аналіз основних показників діяльності підприєств
"""
from data_service import get_dovidnyk, get_osnovni_pokaznyky

# cловник в якому будуть накопичуватись результати розрахунків
index = {
    'index_name'  : '',      #назва підприємства
    'area'        : 0.0,      #одиниця виміру
    'period'         : '',      #період
    'circulation'  : 0.0,     #роздрібний товарообіг
    'income'    : 0.0,     #рівень валового доходу
    'loss'   : 0.0,     #рівень витрат обігу 
    'profit' : 0.0,     #балансовий прибуток 
    'clear profit': 0.0,     #чистий прибуток
}

def create_analiz():
    """формування списку даних аналізу основних показників
    діяльності підприємтсва
    
    Returns:
        indexes_list: список даних
    """

    def get_index_name(index_name_code):
        """знаходить назву показника по коду
        Args:
            index_name_code ([type]): код назви показника
        
        Returns:
            [type]: назву показників
        """

        for index_name in dovidnyk:
            if index_name_code == index_name[0]:
                return (index_name[1])
        
        return "*** назва показника не знайдена"

    def get_area(area_code):
        """знаходить площу по коду
        Args:
            unit_code ([type]): код одиниці виміру
        
        Returns:
            [type]: одиницю виміру   
        """
        
        for area in dovidnyk:
            if area_code == area[0]:
                return (area[2])
        
        return "*** одиниця виміру не знайдена"

    # накопичувач результатів
    index_list = []
    
    dovidnyk = get_dovidnyk()
    osnovni_pokaznyky = get_osnovni_pokaznyky()

    for pokaznyk in osnovni_pokaznyky:

        # робоча копія
        index_work = index.copy()

        index_work['period']           = pokaznyk[2]
        index_work['circulation']    = pokaznyk[3]
        index_work['income']      = pokaznyk[4]
        index_work['loss']     = pokaznyk[5]
        index_work['profit']   = pokaznyk[6]
        index_work['clear profit']  = pokaznyk[7]
        index_work['index_name']    = get_index_name(pokaznyk[1])
        index_work['area']          = get_area(pokaznyk[2])
        
        index_list.append(index_work)

    return index_list

# indexes = create_analiz()
# for item in indexes:
#     print(item)
