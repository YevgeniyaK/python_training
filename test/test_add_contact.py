# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string
import re

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return clear_spaces(prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]))

def random_string_letters(prefix, maxlen):
    symbols = string.ascii_letters + " "*10
    return clear_spaces(prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]))

def random_string_numbers(prefix, maxlen):
    symbols = string.digits + " "
    return clear_spaces(prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]))

def random_title():
    titles = ["Mr.", "Ms.", "Mrs.", "Dr."]
    return random.choice(titles)

#очищаем двойные пробелы и пробелы в начале и в конце
def clear_spaces(s):
    return re.sub("\s\s", " ", s).strip(" ")

testdata = [Contact(firstname=random_string_letters("firstname", 10), middlename=random_string_letters("middlename", 10), lastname=random_string_letters("lastname", 10),
                                             nickname=random_string_letters("nickname", 10), title=random_title(), company=random_string_letters("company", 10),
                                             address=random_string("address", 10),
                                             phone_home=random_string_numbers("+", 10), phone_mobile=random_string_numbers("+", 10),
                                             phone_work=random_string_numbers("+", 10),
                                             fax_number=random_string_numbers("fax", 10), email="test@mail.ru", email2="ya@ya.ru", email3="test@gmail.com",
                                             homepage="http://example.com", birthday_day="21", birthday_month="12",
                                             birthday_year="1990", anniversary_day="18", anniversary_month="10",
                                             anniversary_year="2010", secondary_address="1234567",
                                             secondary_phone=random_string_numbers("+", 10), notes=random_string_letters("notes", 10))
            for i in range(2)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contacts.get_contacts_list()
    app.contacts.add_new_contact(contact)
    #получаем список контактов и сразу сортируем его
    new_contacts = app.contacts.get_contacts_list()
    new_contacts = sorted(new_contacts, key=Contact.id_or_max)

    assert len(old_contacts) + 1 == len(new_contacts)
    #сохраняем id добавленного контакта
    contact.id = new_contacts[len(new_contacts)-1].id
    old_contacts.append(contact)

    assert sorted(old_contacts, key=Contact.id_or_max) == new_contacts
