# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.add_new_contact(Contact(firstname="Firstname", middlename="Middlename", lastname="Lastname",
                         nickname="Nickname", title="Mr", company="Company", address="Address line",
                         phone_home="+74951234567", phone_mobile="+79031234567", phone_work="+74961234567",
                         fax_number="+74961234560", email="test@mail.ru",
                         homepage="http://example.com", birthday_day="21", birthday_month="12",
                         birthday_year="1990", anniversary_day="18", anniversary_month="10",
                         anniversary_year="2010", secondary_address="secondary address",
                         home_address="home address", notes="notes"))
    app.logout()


