import re

text = "Что такое Регулярные Выражения и как их использовать?!  Говоря простым языком, РЕГУЛЯРНОЕ выраЖение — это последовательность символов, используемая для поиска и замены текста в строке или файле... Как уже было упомянуто, их поддерживает множество языков общего назначения: Python, Perl, R.Так что изучение регулярных выражений рано или поздно пригодится?"

pattern = r"регулярн\w+ выражен\w+"
result = re.findall(pattern, text, re.IGNORECASE|re.U)
print(result)


result_ = re.match(pattern,text)
print(result)
print(result.group())   # достать результат поиска.
print(result.start(), result.end())     #достать границы вхождения.

#найти первый попавшийся .
result_ = re.search(pattern,text)
print(result)
print(result.group())   # достать результат поиска.
print(result.start(), result.end())     #достать границы вхождения.

pattern = r"\w+"
# найти все варианты (все слова)
words_list = re.findall(pattern, text)
# print(len(words_list), words_list)

# найти все предложения
pattern = r"[?!.]+\s*"
sent_list = re.split(pattern, text)
sent_list.remove("")
# print(len(sent_list), sent_list)

result = re.findall(r"[^?!.]+[?!.]+\s*", text)
# print(result)

# получить предложения и то, на что они заканчиваются
sent_list = []
delimiters_list = []
positions_list = []
shift = 0
while True:
	result = re.search(pattern, text[shift:])
	# print(result)
	if result is None:
		break

	delimiters_list.append(result.group())
	sent_list.append(text[:result.start()])
	shift += result.end()
	positions_list.append((result.start(), result.end()))
	# text = text[shift:]
		

# print(sent_list)
# print(delimiters_list)
# print(positions_list)

# pattern = r"регулярн\w+ выражен\w+"
# result = re.findall(pattern, text)
# print(result)
# # найти первый попавшийся
# result = re.match(pattern, text)
# print(result)
# result = re.search(pattern, text)
# print(result)

# result = re.search(r"^регулярн\w+ выражен\w+", text)
# print(result)

# result = re.search(r"пригодится\?$", text)
# print(result)

# print(result)
# print(result.group(0))
# print(result.start(), result.end())

# найти первый попавшийся
# result = re.search(pattern, text)
# print(result)
# print(result.group(0))
# print(result.start(), result.end())

text2 = '''хгалтер; Мазин Александр Александрович; Заместитель начальника санатория; Нехай Тимур Нальбиевич;Заместитель начальника санатория-начальник филиала ""Лесная сказка""; Рудницкая Любовь Николаевна; Заместитель начальника санатория по медицинской части - врач-специалист; Шлыков Анатолий Константинович;Заместитель начальника санатория-начальник филиала ""Кабардинка""";http://customs.ru/index.php?option=com_content&view=article&id=8018&Itemid=1878;354037, Краснодарский край, г. Сочи, Новороссийское шоссе, д. 2;2,30E+18;52243166;1,02E+12;2319027603;pobeda@sochi.com;8 (862)265-88-29;8 (862)265-88-25;"Заместитель начальника санатория: 8 (862) 265-88-22; Главный бухгалтер: 8 (862) 265-88-93; Заместитель начальника санатория по медицинской части - врач-специалист: 8 (862) 265-88-24; Приемная филиала ""Лесная сказка"": 8 (8777) 2-94-51; Приемная филиала ""Кабардинка"": 8 (86141) 6-57-45                                                             ";http://www.pobeda-sochi.ru
"Государственное казенное учреждение ""Санаторий ""Электроника"" ФТС России""";"Санаторий ""Электроника"" ФТС России";"Морозов Филипп Александрович; Начальник санатория";"Ангилов Василий Александрович; Заместитель начальника санатория по медицинской части";http://customs.ru/index.php?option=com_content&view=article&id=8018&Itemid=1878;"357700, Ставропольский край, 
г. Кисловодск, ул. Желябова, д.14
";2,60E+18;7548876;1,07E+12;2628050110;"medreg67886@mail.ru; info@electron-kmv.ru"; 8 (87937) 6-73-41;" 8 (87937) 6-78-86;  8 (87937) 2-90-81";" Регистратура: 8 (87937) 6-78-86; Администрация: 8 (87937) 6-73-48; Начальник санатория: 8 (87937) 6-73-80; Начальник медицинской части: 8 (87937) 2-75-66; Бухгалтерия: 8 (87937) 6-74-02; Приемная: (87937) 6-73-41";http://www.electron-kmv.ru
"Государственное казенное учреждение "" Центральный клинический госпиталь ФТС России""";Центральный клинический госпиталь ФТС России;"Дасаев Николай Александрович; Начальник госпиталя";"Седых Юрий Петрович; Заместитель начальника госпиталя по медицинской части";http://customs.ru/index.php?option=com_content&view=article&id=8018&Itemid=1878;107143, г. Москва, Открытое шоссе, дом 32;7,70E+18;59041632;1,03E+12;7730156050;info@hospitalfts.ru;8 (495)781-03-23;8 (495) 781-03-08;"Заместитель начальника госпиталя по медицинской части: 8 (495) 781-03-58; Главный бухгалтер: 8 (495) 781-03-67; Заместитель начальника госпиталя по хозяйственным вопросам: 8 (495) 781-03-31; Кабинет оформления медицинских услуг:  8 (985) 771-47-00                                                            ";http://hospitalfts.ru
"Государственное казенное учреждение ""Центральная поликлиника ФТС России""";Центральная поликлиника ФТС России;"Григорьев Максим Эдуардович; начальник поликлиники";"Несук Ольга Михайловна; ";http://customs.ru/index.php?option=com_content&view=article&id=8018&Itemid=1878;"105118;г.Москва;ул.Шоссе Энтузиастов;д.42";7,70E+18;56670630;1,04E+12;7730140003;cpfts@mail.ru;(495) 276-40-90;"8(495) 276-41-24; 8(495)276-41-25";"бухгалтерия; (495)276-40-79";http://www.policlinika-fts.ru
Государственное казенное образовательное учреждение высшего профессионального образования «Российская таможенная академия»;Российская таможенная академия;Мантусов Владимир Бадьминович, начальник академии;, первый проректор;http://rta.customs.ru/rta/index.php?option=com_content&view=article&id=796&Itemid=2097;140009, Московская область, г. Люберцы, Комсомольский проспект, дом 4;5,00E+18;29884296;1,04E+12;5027053224;rta2009@mail.ru;(495) 503 77 '''

pattern = r"(8|\+7)?\s*\((\d+)\)\s*(\d+)[-\s]*(\d+)[-\s]*(\d+)"
result = re.sub(pattern, r"+7(\2)\3-\4-\5", text2)
# print(result)

phones_list = re.findall(pattern, text2)
# print(phones_list)
# print(" ".join(phones_list[0]))

# phone = re.search(pattern, text2)
# print(phone)
# print(phone.group(0))
# print(phone.group(1))
# print(phone.group(2))
# print(phone.group(3))
# print(phone.group(4))
# print(phone.group(5))


# pattern = r"(8|\+7)?\s*\((\d+)\)\s*(\d+)[-\s]*(\d+)[-\s]*(\d+)"
# pattern_comp = re.compile(r"(8|\+7)?\s*\((\d+)\)\s*(\d+)[-\s]*(\d+)[-\s]*(\d+)")

# print(type(pattern))
# print(type(pattern_comp))

# result = re.findall(pattern, text2)
# result2 = pattern_comp.findall(text2)

# print(result)
# print()
# print(result2)