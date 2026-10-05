import re

def snake_to_camel(snake_str):
    # Находим символ подчеркивания и следующую за ним букву и делаем её заглавной
    components = snake_str.split('_')
    return components[0] + ''.join(x.capitalize() for x in components[1:])

# Пример проверки:
text = "my_long_variable_name"
print(snake_to_camel(text)) # Выведет: myLongVariableName