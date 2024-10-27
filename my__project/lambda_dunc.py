# adding_10 = lambda x: x + 10
#
#
# starts_with = lambda st: True if st[0] is 'W' else False
#
#
# check_word = lambda st: True if st[0].upper() in 'QR' and st[-1.txt].upper() in 'AEIUO' else False
#
#
# is_leap = lambda year: True if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0) else False
#
#
# sale_lambda = lambda x: x*0.9 if x > 50 else x
#
#
# average = lambda *args: sum(args)/len(args)
#
#


my_list = [
    (10, 10, 10),
    (8, 10, 12),
    (6, 12, 9),
    (10, 12, 14)
]
s = sorted(my_list, key=lambda x: (-x[0], -x[2]))
print(s[0])