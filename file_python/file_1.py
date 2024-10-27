# try:
#     with open('hello.txt', encoding='utf-8') as file:
#         s = file.readlines()
#         print(s)
# except FileNotFoundError:
#     print('File not found')
# except:
#     print('Something went wrong')
# finally:
#     print(f'Файл закрыт: {file.close()}')



# clients_bank = [
#     'Narek Arnoevich',
#     'Karen Davlat',
#     'Martun Djuaryan',
#     'Davidik'
# ]
#
# try:
#     with open('file.txt', 'rt+') as file:
#         for line in clients_bank:
#             file.write(line)
# except FileNotFoundError as e:
#     print(f'Ошибка при работе в файлом: {e}')


# try:
#     with open('car.jpg', 'rb') as file:
#         context = file.read()
#         print(context)
#         print(type(context))
# except FileNotFoundError:
#     print('File not found')


# filename = 'data.csv'
#
# # Записываем данные в файл
# with open(filename, 'w') as file:
#     file.write("Python is awesome!\n")
#     file.write("This is a new line.\n")
#
# # Читаем данные из файла
# with open(filename, 'r') as file:
#     content = file.read()
#     print(content)


# import csv
#
# with open('data.csv', mode='r', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(*row, end='\t')

# import csv
#
# data = [
#     ['Name', 'Age', 'City'],
#     ['John', 28, 'New York'],
#     ['Anna', 22, 'London'],
#     ['Mike', 32, 'San Francisco']
# ]
#
# with open('output.csv', mode='w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)


# with open('file_1.txt') as file:
#     # print(file.readlines())
#
#     # for line in file.readlines():
#     #     print(line.strip())
#
#     for line in file:
#         print(line.strip())

# my_str = 'Hack The Planet'
# my_str2 = 'Hack The Sea'
# password_list = ['1234qwer', 'qwerasdf', 'zxcvbnm1']
#
# with open('my_file.txt', 'w') as file:
#     file.writelines([my_str, my_str2, str(password_list)])


# def document_it(func):
#     def wrapper(*args, **kwargs):
#         print('Running function {}'.format(func.__name__))
#         return func(*args, **kwargs)
#     return wrapper
#
# @document_it
# def say_hello():
#     print(input("Как дела? "))
#     return
#
# say_hello()


# def log_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"Function {func.__name__} called with {args} and {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"Function {func.__name__} returned {result}")
#         return result
#     return wrapper
#
# @log_decorator
# def add(*args, **kwargs):
#     return args, kwargs
#
# add(2, 3, name='Adrian', k=3.14)


# def check_access(user_role):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if user_role == "admin":
#                 return func(*args, **kwargs)
#             else:
#                 print("Access denied!")
#         return wrapper
#     return decorator
#
# @check_access("admin")
# def sensitive_operation():
#     print("Sensitive operation performed!")
#
# sensitive_operation()


