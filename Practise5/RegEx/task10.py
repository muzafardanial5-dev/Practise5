import re

def camel_to_snake(camel_str):
    # Находим заглавные буквы и вставляем перед ними нижнее подчеркивание
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

# Пример проверки:
text = "myLongVariableName"
print(camel_to_snake(text)) # Выведет: my_long_variable_name