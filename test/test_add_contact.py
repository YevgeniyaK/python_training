# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    contact = Contact(firstname="Firstname", middlename="Middlename", lastname="Lastname",
                      nickname="Nickname", title="Mr", company="Company", address="Address line",
                      phone_home="+74951234567", phone_mobile="+79031234567", phone_work="+74961234567",
                      fax_number="+74961234560", email="test@mail.ru",
                      homepage="http://example.com", birthday_day="21", birthday_month="12",
                      birthday_year="1990", anniversary_day="18", anniversary_month="10",
                      anniversary_year="2010", secondary_address="secondary address",
                      home_address="home address", notes="notes")
    old_contacts = app.contacts.get_contacts_list()
    app.contacts.add_new_contact(contact)
    new_contacts = app.contacts.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    # сохраняем id добавленного контакта
    contact.id = new_contacts[len(new_contacts)-1].id
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
