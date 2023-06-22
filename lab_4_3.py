"""
Дана строка, состоящая только из букв. Заменить все буквы «a» на буквы «б» и наоборот,
как заглавные, так и строчные. Например, при вводе строки «абвАБВ» должен получиться
результат «бавБАВ»

"""

def text(t):
    text_list = []
    for i in range(len(t)):
        text_list.append(t[i])

        if text_list[i] == "а":
            text_list[i] = "б"

        elif text_list[i] == "А":
            text_list[i] = "Б"

        elif text_list[i] == "б":
            text_list[i] = "а"

        elif text_list[i] == "Б":
            text_list[i] = "А"

    s = ''.join(text_list)
    print(s)
    input("")

if __name__ == "__main__":
    text(input("Введите текст: "))
