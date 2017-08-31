# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string
import re

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return clear_spaces(prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]))

#очищаем двойные пробелы и пробелы в начале и в конце
def clear_spaces(s):
    return re.sub("\s\s", " ", s).strip(" ")

testdata = [Group(name="", header="", footer="")] + [
     Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
     for i in range(5)
  ]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




#list comprehention
#testdata = [
#    Group(name=name, header=header, footer=footer)
#    for name in ["", random_string("name", 10)]
#    for header in ["", random_string("header", 20)]
#   for footer in ["", random_string("footer", 20)]
#]
