# # def print_colors() -> None:
# #     def print_red() -> None:
# #         print('red')
# #
# #     def print_blue() -> None:
# #         print('blue')
# #
# #     print_red()
# #     print_blue()
# #
# #
# # print_colors()
#
# # g = 'grey'
# #
# # def print_colors() -> None:
# #     b = 'yellow'
# #
# #     def print_red() -> None:
# #         r = 'red'
# #         print(r, g, b)
# #
# #     def print_blue() -> None:
# #         q = 'blue'
# #         print(q, g, b)
# #
# #     print_red()
# #     print_blue()
# #
# # print_colors()
#
# # def greeting(firstname, lastname):
# #     def concatenate():
# #         return f'{firstname} {lastname}'
# #
# #     print("Добрый день, " + concatenate() + "!")
# #
# #
# # greeting('Олег', 'Барсук')
#
#
# # def print_colors(param = 'r') -> None:
# #
# #     def print_red() -> None:
# #         r = 'red'
# #         print(r)
# #
# #     def print_blue() -> None:
# #         b = 'blue'
# #         print(b)
# #
# #     if param == 'r':
# #         print_red()
# #     elif param == 'b':
# #         print_blue()
# #     else:
# #         print('I do not know this color')
# #
# # print_colors()
# # print_colors('b')
# # print_colors('y')
#
#
# # def wrap_increment(value):
# #     # определите вложенную функцию _inc
# #     def _inc(value):
# #         value += 1
# #         return value
# #     return _inc(value)
# #
# #
# # print(wrap_increment(41))
#
# def get_extensions(file_list):
#     def _get_extension(file_list):
#         results = []
#         for i in file_list:
#             if "." in i:
#                 ext = i.split(".")[-1]
#             else:
#                 ext = ""
#             results.append(ext)
#         return sorted(results, key=len)
#     return _get_extension(file_list)
#
#
# print(get_extensions(["foo.txt1111", "bar.mp44", "python3", 'ardrunio.bm4px5']))


# def do(x):
#     return x ** 2
#
#
# def does(y):
#     return y * 2
#
#
# def my_func(q, w, t):
#     return q(t) - w(t)
#
#
# result = my_func(do, does, 5)
# print(result)