#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def text(t):
    n = 0
    text_list = t.split() # Не удаляется точка и не учитывает регистр
    for i in text_list:
        if i == "или":
            n += 1
    print("Слово (или) встречается - ", n)
    input("")

if __name__ == "__main__":
    text(input("Введите текст со словом - или: "))
