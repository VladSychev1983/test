# -*- coding: utf-8 -*-
documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def get_name(doc_number):
  doc_number = str(doc_number)
  result = ""
  for dic_list in documents:
    if doc_number == dic_list["number"]:
      result = dic_list["name"]
      break
    else:
      result = 'Документ не найден'
  return result

def get_directory(doc_number):
  doc_number = str(doc_number)
  result = ""
  for key, value in directories.items():
    if doc_number in value:
      result = key
      break
    else:
      result = 'Полки с таким документом не найдено'
  return result

def add(document_type, number, name, shelf_number):
  document_type = str(document_type)
  number = str(number)
  name = str(name)
  shelf_number = str(shelf_number)
  if shelf_number in directories.keys():
    documents.append({"type": document_type, "number": number, "name": name})
    directories[shelf_number].append(number)
  else:
    print("Полки с таким номером не существует")
  return documents, directories

if __name__ == '__main__':
  print(get_name("10006"))
  print(get_directory("11-2"))
  print(get_name("101"))
  add('international passport', '311 020203', 'Александр Пушкин', 3)
  print(get_directory("311 020203"))
  print(get_name("311 020203"))
  print(get_directory("311 020204"))