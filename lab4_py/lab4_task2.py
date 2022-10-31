def get_count_char(str_):
     char_dict = {}
     str_ = " ".join(str_)
     str_ = str_.lower()

     for char_ in str_:
         if char_.isalpha() and (char_ not in char_dict):
              char_dict[char_] = 0
         if char_.isalpha() and (char_ in char_dict):
             char_dict[char_] += 1


     return char_dict

def get_percent_char(dict_):
    sum_ = sum(dict_.values())

    for char_ in dict_:
        dict_[char_] = round(dict_[char_]/sum_ * 100, 1)
    char_dict_percent = dict_.copy()

    return char_dict_percent



main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

char_dict = {   # решил для наглядности и простоты устной проверки ввести малый словарь
    'a':3,
    'b':5,
    'c':2,
    'd':0
}

#print(get_percent_char(get_count_char(main_str)))
# print(get_percent_char(char_dict))
