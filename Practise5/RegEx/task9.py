import re

def insert_spaces(text):
    # Добавляем пробел перед каждой заглавной буквой (кроме первой)
    result = re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
    print("Результат:", result)

# Пример проверки:
text = "HelloWorldPython"
insert_spaces(text) # Выведет: Hello World Python