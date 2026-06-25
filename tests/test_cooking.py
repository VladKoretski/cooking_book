import unittest
import tempfile
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # чтобы импортировать cooking

import cooking  # ваш файл cooking.py

class TestCookingBook(unittest.TestCase):
    def setUp(self):
        # Создаём временный файл с рецептами
        self.test_file = tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8')
        self.test_file.write("""Омлет
3
Яйцо | 2 | шт
Молоко | 100 | мл
Помидор | 2 | шт

Утка по-пекински
4
Утка | 1 | шт
Вода | 2 | л
Мед | 3 | ст.л
Соевый соус | 60 | мл
""")
        self.test_file.close()
        self.filepath = self.test_file.name

    def tearDown(self):
        os.unlink(self.filepath)

    def test_line_parcing(self):
        result = cooking.line_parcing('Яйцо | 2 | шт')
        expected = {'ingredient_name': 'Яйцо', 'quantity': '2', 'measure': 'шт'}
        self.assertEqual(result, expected)
        self.assertTrue(cooking.line_parcing('Название блюда'))

    def test_file_into_dictionary_recipes(self):
        cook_book = cooking.file_into_dictionary_recipes(self.filepath)
        self.assertIn('Омлет', cook_book)
        self.assertEqual(len(cook_book['Омлет']), 3)
        self.assertEqual(cook_book['Омлет'][0]['ingredient_name'], 'Яйцо')
        self.assertEqual(cook_book['Утка по-пекински'][0]['measure'], 'шт')

    def test_get_shop_list(self):
        # Заполняем глобальную переменную cook_book в модуле cooking
        cooking.cook_book = cooking.file_into_dictionary_recipes(self.filepath)
        result = cooking.get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2)
        # Так как 'Запеченный картофель' отсутствует в тестовом файле, он будет проигнорирован
        self.assertIn('Яйцо', result)
        self.assertEqual(result['Яйцо']['quantity'], 4)
        # Проверяем, что отсутствующее блюдо не вызывает ошибки
        cooking.get_shop_list_by_dishes(['Несуществующее'], 1)  # просто проверяем, что не падает

if __name__ == '__main__':
    unittest.main()