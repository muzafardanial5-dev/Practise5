import re

def find_sequences(text):
    pattern = r"[a-z]+_[a-z]+"
    matches = re.findall(pattern, text)
    print("Найденные последовательности:", matches)

# Пример проверки:
text = "hello_world test_string Test_string hello-world snake_case"
find_sequences(text) # Найдет: ['hello_world', 'test_string', 'snake_case']