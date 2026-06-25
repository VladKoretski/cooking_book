import os

path_to_file = os.path.join(os.getcwd(), 'recipes.txt')
cook_book = dict()


def line_parcing(line_with_ingrdients):
    """
    Парсит строку с ингредиентом в формате "Название | Количество | Единица".
    """
    dict_with_ingredients = dict()

    if '|' in line_with_ingrdients:
        dict_with_ingredients['ingredient_name'] = line_with_ingrdients.split(' | ')[0]
        dict_with_ingredients['quantity'] = line_with_ingrdients.split(' | ')[1]
        dict_with_ingredients['measure'] = line_with_ingrdients.split(' | ')[2]
        return dict_with_ingredients
    else:
        return True


def file_into_dictionary_recipes(recipes_file):
    """
    Читает файл с рецептами и возвращает словарь cook_book.
    """
    cook_book_dict = dict()
    with open(recipes_file) as f:

        for line in f:
            data = line.strip()
            if not data:
                continue
            try:
                _ = int(data)
            except ValueError:
                if line_parcing(data):
                    cook_book_dict[data] = []
                    current_key = data
                else:
                    cook_book_dict[current_key].append(line_parcing(data))
    return cook_book_dict


def get_shop_list_by_dishes(dishes, person_count):
    """
    Рассчитывает общее количество ингредиентов для заданных блюд.
    """
    shop_list = dict()
    for dish in dishes:
        try:
            for i in range(len(cook_book[dish])):
                ingredient = cook_book[dish][i]
                ingredient_name = ingredient['ingredient_name']
                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {
                        'measure': ingredient['measure'],
                        'quantity': int(ingredient['quantity']) * person_count
                    }
                else:
                    shop_list[ingredient_name]['quantity'] += (
                        int(ingredient['quantity']) * person_count
                    )
        except KeyError:
            print(f'{dish} not in {cook_book}')
    return shop_list
