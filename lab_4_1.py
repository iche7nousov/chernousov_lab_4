"""
16. Дано предложение. Определить число пробелов в нем.
"""

def get_number_space(text):
    n = 0
    for i in text:
        if i.isspace():
            n += 1
    print(f"Количество пробелов - {n}")
    input("")
if __name__ == "__main__":
    get_number_space(input("Введите текст: "))