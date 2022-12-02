with open('referat.txt', 'r', encoding='utf-8') as referat_1:
    data_from_file = referat_1.read()
    len_file = len(data_from_file)
    words_quantity = len(data_from_file.split())
    data_from_file = data_from_file.replace('.', '!')

with open('referat2.txt', 'w', encoding='utf-8') as referat_2:
    referat_2.write(f'Длина старого файла: {len_file}\n')
    referat_2.write(f'Количество слов в старом файле: {words_quantity}\n')
    referat_2.write(data_from_file)