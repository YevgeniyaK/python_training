# -*- coding: utf-8 -*-
from model.group import Group
import pytest

def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    with pytest.allure.step("Given a group list"):
        old_groups = db.get_group_list()
    with pytest.allure.step("When I add group %s to the list" % group):
        app.group.create(group)
    with pytest.allure.step("Then the new group list is equal to the old list with the added group"):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    if check_ui:
        app_groups = app.group.get_group_list()
        for new_group in new_groups:
            for app_group in app_groups:
                if new_group.id == app_group.id:
                    assert new_group.name == app_group.name
                    break




#list comprehention
#testdata = [
#    Group(name=name, header=header, footer=footer)
#    for name in ["", random_string("name", 10)]
#    for header in ["", random_string("header", 20)]
#   for footer in ["", random_string("footer", 20)]
#]
#@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
