#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

if __name__ == "__main__":
    text(input("Введите текст: "))
