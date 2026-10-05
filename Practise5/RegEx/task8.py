import re

def split_by_uppercase(text):
    # Разбиваем строку перед каждой заглавной буквой
    parts = re.findall(r'[A-Z][^A-Z]*', text)
    print("Результат разбиения:", parts)

# Пример проверки:
text = "HelloWorldPython"
split_by_uppercase(text) # Выведет: ['Hello', 'World', 'Python']