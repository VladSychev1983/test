# -*- coding: utf-8 -*-
"""
Будем помогать Распределяющей Шляпе направлять начинающих магов в подходящие им факультеты.

Для каждого факультета у нас определен список характерных для него качеств и есть словарь наших магов с их чертами характера.
"""
houses_traits = {
    'Slytherin': ['хитрость', 'находчивость', 'амбициозность'],
    'Gryffindor': ['храбрость', 'благородство', 'честность'],
    'Hufflepuff': ['честность', 'верность', 'трудолюбие'],
    'Ravenclaw': ['мудрость', 'ум', 'творчество']
}

new_magicians = {
    'Arabella Skeeter': ['хитрость', 'творчество', 'находчивость'],
    'Stan Malfoy': ['амбициозность', 'благородство', 'храбрость'],
    'Morgana Granger': ['трудолюбие', 'верность', 'мудрость']
}

for name, p_traits in new_magicians.items():
    # print(name)
    # print(p_traits)
    matches = {}
    for house, h_traits in houses_traits.items():
        matches[house] = len(set(h_traits) & set(p_traits))
    #print(f'{name} - {matches}')
    print(name,'-',matches)
    
    # dict comprehension "стиль понимания"
    for name, p_traits in new_magicians.items():
    matches = {house: len(set(h_traits) & set(p_traits)) for house, h_traits in houses_traits.items()}
    #print(f'{name} - {matches}')
    print(name,'-',matches)