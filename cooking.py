import os

path_to_file = os.path.join(os.getcwd(), 'recipes.txt')
cook_book = dict()

def line_parcing(line_with_ingrdients):
    """
    Парсит строку с ингредиентом в формате "Название | Количество | Единица".

    Аргументы:
        line_with_ingrdients (str): строка для парсинга.

    Возвращает:
        dict или bool: если строка содержит '|', возвращает словарь с ключами
        'ingredient_name', 'quantity', 'measure'. Если '|' отсутствует,
        возвращает True (это используется для определения названия блюда).

    Пример:
        >>> line_parcing('Яйцо | 2 | шт')
        {'ingredient_name': 'Яйцо', 'quantity': '2', 'measure': 'шт'}
    """

    dict_with_ingredients = dict() 

    if '|' in line_with_ingrdients:
        dict_with_ingredients['ingredient_name'] = line_with_ingrdients.split(' | ')[0]
        dict_with_ingredients['quantity'] = line_with_ingrdients.split(' | ')[1]
        dict_with_ingredients['measure'] = line_with_ingrdients.split(' | ')[2]
        return dict_with_ingredients
    else:
        return True
   
    
def file_into_dictionary_recipes (recipes_file):
    """
    Читает файл с рецептами и возвращает словарь cook_book.

    Формат файла описан в условии задачи. Функция ожидает, что в файле
    строки с названиями блюд, затем число ингредиентов, затем сами ингредиенты
    в формате "Название | Количество | Единица". Пустые строки пропускаются.

    Аргументы:
        recipes_file (str): путь к файлу с рецептами.

    Возвращает:
        dict: словарь вида {название_блюда: [список_ингредиентов]}, где
        каждый ингредиент — словарь с ключами 'ingredient_name', 'quantity', 'measure'.
        Количество сохраняется как строка.

    Примечание:
        Функция не использует число ингредиентов для ограничения цикла,
        а полагается на структуру файла (название блюда не содержит '|' и не является числом).

    Пример:
        >>> cook = file_into_dictionary_recipes('recipes.txt')
        >>> 'Омлет' in cook
        True
    """

    cook_book_dict = dict()
    with open (recipes_file) as f:
        
        for line in f:
            data = line.strip()
            if not data:
                continue
            try:
                number = int(data)            
            except ValueError:
                if line_parcing(data) == True:
                    cook_book_dict[data] = []
                    current_key = data
                else:
                    cook_book_dict[current_key].append(line_parcing(data))
    return(cook_book_dict)


def get_shop_list_by_dishes(dishes, person_count):
    """
    Рассчитывает общее количество ингредиентов для заданных блюд на указанное число персон.

    Аргументы:
        dishes (list): список названий блюд (строк).
        person_count (int): количество человек.

    Возвращает:
        dict: словарь, где ключ — название ингредиента, значение — словарь
        с ключами 'measure' и 'quantity' (количество уже умножено на person_count).

    Примечание:
        Используется глобальная переменная cook_book, которая должна быть
        предварительно заполнена функцией file_into_dictionary_recipes.
        Если блюдо отсутствует в cook_book, выводится сообщение и оно игнорируется.

    Пример:
        >>> cook_book = file_into_dictionary_recipes('recipes.txt')
        >>> get_shop_list_by_dishes(['Омлет'], 2)
        {'Яйцо': {'measure': 'шт', 'quantity': 4}, ...}
    """

    shop_list = dict()
    for dish in dishes:
        try:
            for i in range(len(cook_book[dish])):
                if cook_book[dish][i]['ingredient_name'] not in shop_list:
                    shop_list[cook_book[dish][i]['ingredient_name']] = {'measure': cook_book[dish][i]['measure'], 'quantity': int(cook_book[dish][i]['quantity']) * person_count}
                else:
                    shop_list[cook_book[dish][i]['ingredient_name']]['quantity'] += int(cook_book[dish][i]['quantity']) * person_count 
        except KeyError:
            print(f'{dish} not in {cook_book}')        
    return shop_list