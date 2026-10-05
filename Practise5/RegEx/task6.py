import re

def replace_characters(text):
    # Ищем пробел, запятую или точку
    pattern = r"[ ,.]"
    new_text = re.sub(pattern, ":", text)
    print("Результат замены:", new_text)

# Пример проверки:
text = "Привет, мир. Как дела? Все хорошо."
replace_characters(text) # Выведет: Привет::мир::Как:дела?:Все:хорошо.