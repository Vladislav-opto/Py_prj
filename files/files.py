def len_qnt_file(my_file):
    with open(my_file, 'r', encoding='utf-8') as my_file:
        data_from_file = my_file.read()
    print(f'Длина старого файла: {len(data_from_file)}')
    print(f'Количество слов в старом файле: {len(data_from_file.split())}')
    data_from_file = data_from_file.replace('.', '!')
    return(data_from_file)


def write_to_file(my_file, data_from_file):
    with open(my_file, 'w', encoding='utf-8') as my_file:
        my_file.write(data_from_file)


if __name__ == "__main__":
    write_to_file('referat2.txt', len_qnt_file('referat.txt'))