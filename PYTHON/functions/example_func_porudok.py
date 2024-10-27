
"""
    Программа для поиска совпадений между
    двумя списками, используя функцию filter()
"""


list1 = ["Python", "CSharp", "Java", "Go"]
list2 = ["Python", "Scala", "JavaScript", "Go", "PHP", "CSharp"]


def filter_duplicate(string_to_check):
    if string_to_check in ll:
        return False
    else:
        return True


ll = list2
out_filter = list(filter(filter_duplicate, list1))
ll = list1
out_filter += list(filter(filter_duplicate, list2))

print("Отфильтрованный список:", out_filter)

print(__doc__)
