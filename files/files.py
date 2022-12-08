def print_result(input_data: dict) -> None:
    for n in input_data:
        print (f'{n}: {input_data[n]}')


def replace_in_file(input_file: str) -> str:
    with open(input_file, 'r', encoding='utf-8') as file_handler:
        data_from_file = file_handler.read()
    data_from_file = data_from_file.replace('.', '!')
    return data_from_file


def len_qnt_words_file(input_file: str) -> str:
    dict_result = {}
    with open(input_file, 'r', encoding='utf-8') as file_handler:
        data_from_file = file_handler.read()
    len_file = len(data_from_file)
    quantity_words = len(data_from_file.split())
    dict_result['Длина файла'] = len_file
    dict_result['Количество слов в файле'] = quantity_words
    return dict_result


def write_to_file(file_output: str, data_from_file: str) -> None:
    with open(file_output, 'w', encoding='utf-8') as file_handler:
       file_handler.write(data_from_file)


if __name__ == "__main__":
    print_result(len_qnt_words_file('referat.txt'))
    write_to_file('referat2.txt', replace_in_file('referat.txt'))