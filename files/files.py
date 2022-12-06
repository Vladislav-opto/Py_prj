def print_result(preamble, data_to_print):
    print(f'{preamble}: {data_to_print} ед.')


def len_qnt_file(input_file):
    with open(input_file, 'r', encoding='utf-8') as file_handler:
        data_from_file = file_handler.read()
    len_file = len(data_from_file)
    quantity_word = len(data_from_file.split())
    print_result('Длина старого файла', len_file)
    print_result('Количество слов в старом файле', quantity_word)
    data_from_file = data_from_file.replace('.', '!')
    return data_from_file


def write_to_file(file_output, data_from_file):
    with open(file_output, 'w', encoding='utf-8') as file_handler:
       file_handler.write(data_from_file)


if __name__ == "__main__":
    write_to_file('referat2.txt', len_qnt_file('referat.txt'))