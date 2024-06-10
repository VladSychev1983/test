"""
Покапать можно только брендированные диски из manufacturers , наличие 1 -есть 0-не available
Сколько дисков может купить сисадмин , нужно посчитать количество и вывести список?
"""
repair_count = 0
ssds = []

models = [
    '480 ГБ 2.5" SATA накопитель Kingston A400', 
    '500 ГБ 2.5" SATA накопитель Samsung 870 EVO', 
    '480 ГБ 2.5" SATA накопитель ADATA SU650', 
    '240 ГБ 2.5" SATA накопитель ADATA SU650', 
    '250 ГБ 2.5" SATA накопитель Samsung 870 EVO', 
    '256 ГБ 2.5" SATA накопитель Apacer AS350 PANTHER', 
    '480 ГБ 2.5" SATA накопитель WD Green', 
    '500 ГБ 2.5" SATA накопитель WD Red SA500'
]
available = [1, 1, 1, 1, 0, 1, 1, 0]
manufacturers = ['Intel', 'Samsung', 'WD']

for model,available in zip(models,available):
    #print(model,available)
    for brand in manufacturers:
        if model.count(brand) and available == 1:
            repair_count += 1
            ssds.append(model)
            #print(model)
print(ssds)
print('Sysadmin can repair:',repair_count)

        


