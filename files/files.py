def replace_in_file(input_file):
    with open(input_file, 'r', encoding='utf-8') as file_handler:
        data_from_file = file_handler.read()
    data_from_file = data_from_file.replace('.', '!')
    return data_from_file


def len_qnt_words_file(input_file):
    with open(input_file, 'r', encoding='utf-8') as file_handler:
        data_from_file = file_handler.read()
    len_file = len(data_from_file)
    quantity_word = len(data_from_file.split())
    len_qnt_words = 'Длина старого файла ' + str(len_file) + '\n' + 'Количество слов в старом файле ' + str(quantity_word)
    return len_qnt_words


def write_to_file(file_output, data_from_file):
    with open(file_output, 'w', encoding='utf-8') as file_handler:
       file_handler.write(data_from_file)


if __name__ == "__main__":
    print(len_qnt_words_file('referat.txt'))
    write_to_file('referat2.txt', replace_in_file('referat.txt'))