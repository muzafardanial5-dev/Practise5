import re

def find_capitalized(text):
    pattern = r"[A-Z][a-z]+"
    matches = re.findall(pattern, text)
    print("Найденные слова:", matches)

# Пример проверки:
text = "Hello World python Programming Language"
find_capitalized(text) # Найдет: ['Hello', 'World', 'Programming', 'Language']