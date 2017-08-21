from model.group import Group


def test_add_group(app):
    app.group.change_group(Group(name="updated", header="updated", footer="changed"))
