import json, io, pprint


def add_categories_to_file(input_category: io.TextIOWrapper, input_check: io.TextIOWrapper) -> io.TextIOWrapper:
    with open(input_category, "r", encoding='utf-8') as read_file:
        categories = json.load(read_file)
    with open(input_check, "r", encoding='utf-8') as read_file:
        check_verified = json.load(read_file)
    for number, good in enumerate(check_verified): #нумерация и перебор словарей в чеке от Саши
        key_name = good.get("name", "пусто").replace(".", " ").replace(",", " ").replace("/", " ")
        good_as_list = key_name.lower().split()
        for category in categories:
            for word in good_as_list:
                if word in categories[category]:
                    check_verified[number]["категория"] = category
    return check_verified


if __name__ == "__main__":
    pprint.pprint(add_categories_to_file("category.json", "verified_check.json"))