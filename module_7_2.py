from pprint import pprint


def custom_write(file_name, string):
    file = open(file_name, 'w', encoding='utf8')
    for i, strings in enumerate(string, 1):
        my_tuple = i, file.tell()
        file.write(strings)
        my_dict = my_tuple, strings
        pprint(my_dict)
    file.close()


info = ['Text for tell\n', 'Используйте кодировку utf-8\n',
        'Because there are 2 languages!\n', 'Спасибо!\n']

custom_write('temp.txt', info)
