import re
import csv
from pprint import pprint

FILE_CSV = 'phonebook_raw.csv'

def read_file():

    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        result_dict = {}

        for row in contacts_list:
            mylist = [] 
            mystr = " ".join(row[0:3])
            list_names = mystr.split()
            #записываем фио на свои места.
            if 0 <= 2 < len(list_names):
                row[0], row[1], row[2] = list_names[0], list_names[1], list_names[2]
            else:
                row[0], row[1] = list_names[0], list_names[1]
            mylist.append(row)
            for item in mylist:
                    if f"{item[0]} {item[1]}" not in result_dict:
                        result_dict[f"{item[0]} {item[1]}"] = item
                    else:
                        for count, i in enumerate(item):
                            if result_dict[f"{item[0]} {item[1]}"][count] == i:
                                pass
                        else:
                            if i:
                                result_dict[f"{item[0]} {item[1]}"][count] = i
        #print(result_dict)
        # нормализуем номера.
        contacts_list_result = []
        for value in result_dict.values():
            clear_phone = check_phone(value[5])
            value[5] = clear_phone
            contacts_list_result.append(value)
        
        #print(result_dict)
        write_result(contacts_list_result)


def check_phone(phone):
    pattern = r"^(8|\+7)\s?\(?(\d{3})\)?[\s-]?(\d{3})[-]?(\d{2})[-]?(\d{2})"
    result = re.sub(pattern, r"+7(\2)\3-\4-\5", phone)
    pattern2 = r"^(.*)\s+\(?(\w+\.)\s+(\d+)\)?$"
    result2 = re.sub(pattern2, r"\1 \2\3.", result)
    return result2


def write_result(contacts_list):
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)

if __name__ == '__main__':
    read_file()
