# Асядовский Станислав
import json
print('start code')
with open('dump.json', encoding='utf-8') as file:
    data = json.load(file)
find_qualification = int(input('Введите номер нужной квалификации: '))
flag_found = False
for item in data:
    if item.get('model') == 'data.skill' and item.get('pk') == find_qualification:
        print(f'=============== Найдено ===============')
        print(f'Специальность "{item["fields"].get("specialty")}", ПТО')
        print(f'Квалификация "{item["fields"].get('title')}"')
        flag_found = True
if flag_found == False:
    print('=============== Не найдено ===============')
print('end code')