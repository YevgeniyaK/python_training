from model.group import Group
import random
import pytest


def test_modify_group_name(app, db, check_ui):
    if app.group.count() == 0:
        with pytest.allure.step("Create new group if group list is empty"):
            app.group.create(Group(name="Test"))
    with pytest.allure.step("Given a group list"):
        old_groups = db.get_group_list()
    with pytest.allure.step("choose random group"):
        group = random.choice(old_groups)
    with pytest.allure.step("modify random group"):
        group.name = "new name"
        app.group.modify_group_by_id(group.id, group)
    with pytest.allure.step("Get group list again"):
        new_groups = db.get_group_list()
    with pytest.allure.step("Compare length of old list with length of new list "):
        assert len(old_groups) == len(new_groups)

    if check_ui:
        app_groups = app.group.get_group_list()
        for new_group in new_groups:
            for app_group in app_groups:
                if new_group.id == app_group.id:
                    if new_group.id == group.id:
                        assert new_group.name == group.name
                    else:
                        assert new_group.name == app_group.name
                    break




#def test_modify_group_header(app):
#    if app.group.count() == 0:
#       app.group.create(Group(name="Test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="new header"))
#    new_groups = app.group.get_group_list()
#   assert len(old_groups) == len(new_groups)
# assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
