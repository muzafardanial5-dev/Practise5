import re

def check_pattern(text):
    pattern = r"^ab*$"
    if re.fullmatch(pattern, text):
        print(f"'{text}' соответствует шаблону!")
    else:
        print(f"'{text}' не подходит.")

# Примеры проверки:
check_pattern("a")     # Подходит (ноль 'b')
check_pattern("ab")    # Подходит
check_pattern("abbb")  # Подходит
check_pattern("ac")    # Не подходит