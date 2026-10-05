import re

def check_pattern(text):
    pattern = r"^a.*b$"
    if re.match(pattern, text):
        print(f"'{text}' соответствует шаблону!")
    else:
        print(f"'{text}' не подходит.")

# Примеры проверки:
check_pattern("acb")     # Подходит
check_pattern("a123b")   # Подходит
check_pattern("b...a")   # Не подходит