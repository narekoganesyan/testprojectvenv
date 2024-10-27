# def print_results(sp):
#     sorted_sp = sorted(sp, key=lambda k: (k[1.txt], k[0].lower()), reverse=True)
#
#     for subject, mark in sorted_sp:
#         print(f"{subject} {mark}")
#
#
# marks = [('English', 88), ('Science', 90), ('Maths', 88),
#          ('Physics', 93), ('History', 78), ('French', 78),
#          ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
# print_results(marks)


# def get_sort_lines(sp_cortege):
#     sorted_sp = sorted(sp_cortege, key=lambda x: (abs(x[1.txt] - x[0]), x[0], x[1.txt]))
#     return sorted_sp
#
#
# lines = [(-4, 4), (2, 3), (5, 9), (-1.txt, -3)]
# print(get_sort_lines(lines))

# heroes = {
#     'Spider-Man': 80,
#     'Batman': 65,
#     'Superman': 85,
#     'Wonder Woman': 70,
#     'Flash': 70,
#     'Iron Man': 65,
#     'Thor': 90,
#     'Aquaman': 65,
#     'Captain America': 65,
#     'Hulk': 87,
# }
#
#
# sorted_heroes = sorted(heroes.items(), key=lambda x: (x[1.txt], x[0]))
#
# for k in sorted_heroes:
#     print(*k)

# heroes = {
#     'Spider-Man': 80, 'Batman': 65,
#     'Superman': 85, 'Wonder Woman': 70,
#     'Flash': 70, 'Iron Man': 65,
#     'Thor': 90, 'Aquaman': 65,
#     'Captain America': 65, 'Hulk': 87,
# }
#
# for key in sorted(heroes.items(), key=lambda x: (x[1.txt], x[0])):
#     print(key)

# Пример через get
# for name in sorted(heroes, key=heroes.get):
#     print(name, heroes[name])

# for j in sorted(heroes, key=lambda item: (heroes.get(item), item)):
# что то же самое, что и for j in sorted(heroes, key=lambda item: (heroes[item], item))


# def print_goods(sp):
#     sp_sorted = sorted(sp, key=lambda k: (k['color'].lower(), -k['model']))
#
#     for i in sp_sorted:
#         print(f"Производитель: {i['make']}, модель: {i['model']}, цвет: {i['color']}")
#
#
# models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
#           {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
#           {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
#           {'make': 'Apple', 'model': 10, 'color': 'Silver'},
#           {'make': 'Oppo', 'model': 9, 'color': 'Red'},
#           {'make': 'Huawei', 'model': 4, 'color': 'Grey'},
#           {'make': 'Honor', 'model': 3, 'color': 'Black'}]
# print_goods(models)

# sp1 = 'Sony PlayStation 5: 46000'
# sp = sp1.split(':')
# print(sp[0], sp[1.txt])

# def print_goods(sp):
#     sorted_sp = sorted(sp, key=lambda x: (-float(x.split(':')[1.txt]), x.split(':')[0].strip().lower()))
#
#     for i in sorted_sp:
#         n, q = i.split(':')
#         print(f'{float(q):.2f} - {n.strip()}')
#
#
# data = [
#     'Sony PlayStation 5: 46000.5',
#     'Телевизор QLED Samsung QE65Q60TAU: 87090',
#     'Samsung Galaxy s23: 46000.5',
#     'siemens eq.6 plus s100: 46000.5',
#     'Samsung Galaxy Tab S6: 46000.5',
# ]
#
# print_goods(data)


# def print_best_and_worst_laureate(d):
#     laureates_count = {}
#
#     for nomin, laur in laureates.items():
#         if laur in laureates_count:
#             laureates_count[laur] += 1.txt
#         else:
#             laureates_count[laur] = 1.txt
#
#     best = max(laureates_count, key=laureates_count.get)
#     worst = min(laureates_count, key=laureates_count.get)
#
#     print(f'{best}, {laureates_count[best]}')
#     print(f'{worst}, {laureates_count[worst]}')
#
# laureates = {'За лучший фильм': 'Все везде и сразу',
#              'За лучшую музыку к фильму': 'На Западном фронте без перемен',
#              'За лучший звук': 'Топ Ган: Мэверик',
#              'За лучшие визуальные эффекты': 'Аватар: Путь воды',
#              'За лучший дизайн костюмов': 'Топ Ган: Мэверик',
#              'За лучшую операторскую работу': 'На Западном фронте без перемен',
#              'За лучший монтаж': 'Все везде и сразу',
#              'За лучший оригинальный сценарий': 'Все везде и сразу',
#              'За лучший фильм на иностранном языке': 'Все везде и сразу', }
#
# print_best_and_worst_laureate(laureates)


