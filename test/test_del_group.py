# -*- coding: utf-8 -*-
from model.group import Group
import random
import pytest


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        with pytest.allure.step("Create new group if group list is empty"):
            app.group.create(Group(name="Test"))
    with pytest.allure.step("Given a group list"):
        old_groups = db.get_group_list()
    with pytest.allure.step("choose random group"):
        group = random.choice(old_groups)
    with pytest.allure.step("delete this random group"):
        app.group.delete_group_by_id(group.id)
    with pytest.allure.step("Get group list again"):
        new_groups = db.get_group_list()
    with pytest.allure.step("Compare length of old list with length of new list "):
        assert len(old_groups) - 1 == len(new_groups)
    with pytest.allure.step("Then the new group list is equal to the old list with the added group"):
        old_groups.remove(group)
        assert old_groups == new_groups

    if check_ui:
        app_groups = app.group.get_group_list()
        for new_group in new_groups:
            for app_group in app_groups:
                if new_group.id == app_group.id:
                    assert new_group.name == app_group.name
                    break



'''
Старый тест удаления первой группы
'''
#def test_delete_first_group(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="Test"))
#    old_groups = app.group.get_group_list()
#    app.group.delete_first_group()
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) - 1 == len(new_groups)
#    old_groups [0:1] = []
#    assert old_groups == new_groups
