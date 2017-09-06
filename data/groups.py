from model.group import Group
import random
import string
import re


testdata = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]



#def random_string(prefix, maxlen):
#    symbols = string.ascii_letters + string.digits + " "*10
#    return clear_spaces(prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]))
#
#очищаем двойные пробелы и пробелы в начале и в конце
#def clear_spaces(s):
#    return re.sub("\s\s", " ", s).strip(" ")
#
#testdata = [Group(name="", header="", footer="")] + [
#     Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
#     for i in range(5)
#  ]
