import re
import json

def load_receipt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def extract_prices(text):
    # Задача 1: поиск цен через RegEx
    pass

def find_product_names(text):
    # Задача 2: поиск названий товаров
    pass

def calculate_total(prices):
    # Задача 3: расчет суммы
    pass

def extract_datetime(text):
    # Задача 4: дата и время
    pass

def find_payment_method(text):
    # Задача 5: способ оплаты
    pass

def create_structured_output(data):
    # Задача 6: вывод в JSON или текст
    pass

if __name__ == "__main__":
    receipt_text = load_receipt("raw.txt")
    # Вызов функций и вывод результатов...