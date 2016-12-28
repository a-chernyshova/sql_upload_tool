# -*- coding: utf-8 -*-
import sys
import os

# открыть файл на чтение, сформировать лист строк, закрыть файл
def source():
    string_list = []
    file_list = os.listdir()
    name = input("source file name:")
    name = name + ".txt"
    f = open(name, 'r')
    for line in f:
        string_list.append(line)
    f.close()
    return string_list

# распарсить файл: первая строка - имя таблицы - далее построчно - данные для ввода, разделение запятой
def parse_list(string_list):
    table_name = string_list[0]
    string_list.remove(table_name)
    return table_name
    #for i in range(len(string_list)):
    #    t = str(string_list[i]).split("\n,")


#test = ['people', "ii", 1, 2, 'dfd', 4]
#parse_list(source())
parse_list(source())
print("add raws to ", parse_list(source()))
for i in range(len(source())):
    print(source)
# Обработать исключения

