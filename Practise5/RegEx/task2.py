import re

def check_pattern(text):
    pattern = r"^ab{2,3}$"
    if re.fullmatch(pattern, text):
        print(f"'{text}' соответствует шаблону!")
    else:
        print(f"'{text}' не подходит.")

# Примеры проверки:
check_pattern("abb")   # Подходит (2 буквы 'b')
check_pattern("abbb")  # Подходит (3 буквы 'b')
check_pattern("ab")    # Не подходит (мало)
check_pattern("abbbb") # Не подходит (много)