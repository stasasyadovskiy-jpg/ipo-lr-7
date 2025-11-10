# Асядовский Станислав
# Вариант 2
import json
print('start code')
with open('flowers.json', encoding='utf-8') as file:
        data = json.load(file)
        flowers = data['flowers']
count_actions = 0
while True:
    print(f'1 - Вывести все записи\n2 - Вывести запись по полю\n3 - Добавить запись\n4 - Удалить запись по полю\n5 - Выйти из программы')
    action = int(input("Выберите действие: "))
    print()
    if action == 1:
        count_actions += 1
        for flower in flowers:
            if flower["is_red_book_flower"] == False:
                print(f"============ {flower['name']} ============")
                print(f'Номер цветка - {flower['id']}, Латинское название - {flower['latin_name']}')
                print(f'{flower['name']} не является краснокнижным цветком')
                print(f'=============== Цена: {flower['price']} ===============')
                print()
            elif flower["is_red_book_flower"] == True:
                print(f"============ {flower['name']} ============")
                print(f'Номер цветка - {flower['id']}, Латинское название - {flower['latin_name']}')
                print(f'{flower['name']} является краснокнижным цветком')
                print(f'=============== Цена: {flower['price']} ===============')
                print()      
    elif action == 2:
        count_actions += 1
        num = int(input('Введите ID записи которую хотите вывести: ')) - 1
        found = False
        print()
        if num >= 0 and num < len(flowers):  # проверка, что индекс в пределах списка
            if flowers[num]["is_red_book_flower"] == False:
                print(f"============ {flowers[num]['name']} ============")
                print(f'Номер цветка - {flowers[num]["id"]}, Латинское название - {flowers[num]["latin_name"]}')
                print(f'{flowers[num]["name"]} не является краснокнижным цветком')
                print(f'=============== Цена: {flowers[num]["price"]} ===============')
                print()
                found = True
            elif flowers[num]["is_red_book_flower"] == True:
                print(f"============ {flowers[num]['name']} ============")
                print(f'Номер цветка - {flowers[num]["id"]}, Латинское название - {flowers[num]["latin_name"]}')
                print(f'{flowers[num]["name"]} является краснокнижным цветком')
                print(f'=============== Цена: {flowers[num]["price"]} ===============')
                print()
                found = True
        if not found:
            print("Запись с таким ID не найдена.")
    elif action == 3:
        count_actions += 1
        print('Вы выбрали записать новую запись (новый цветок), вводите данные: ')
        new_flower = {
            "id": int(input("Введите ID: ")),
            "name": input("Введите название цветка: "),
            "latin_name": input("Введите латинское название: "),
            "is_red_book_flower": input("Входит ли в Красную книгу? (true/false): ").strip().lower() == "true",
            "price": input("Введите цену: ")
        }
        data["flowers"].append(new_flower)
        with open('flowers.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("Запись прошла успешно")
    elif action == 4:
        count_actions += 1
        delete_id = int(input("Введите ID записи, которую хотите удалить: "))
        found = False
        for i in range(len(flowers)):
            if flowers[i]["id"] == delete_id:
                del flowers[i]
                found = True
                print(f"Запись с ID {delete_id} удалена.")
                break
        if found == False:
            print(f"Запись с таким ID не найдена.")
        with open('flowers.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    elif action == 5: 
        print(f'Вы провели {count_actions} операций с записями за время работы программы')
        print('Программа завершена')
        break
    else: 
        print('Ошибка ввода, ты идиот')
        break
print('end code')