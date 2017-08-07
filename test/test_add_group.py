# -*- coding: utf-8 -*-
from model.group import


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="12345", header="qwerty", footer="qwertyui"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
