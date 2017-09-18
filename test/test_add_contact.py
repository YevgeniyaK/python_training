# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contacts.add_new_contact(contact)
    #получаем список контактов и сразу сортируем его
    new_contacts = db.get_contact_list()
    new_contacts = sorted(new_contacts, key=Contact.id_or_max)

    assert len(old_contacts) + 1 == len(new_contacts)
    #сохраняем id добавленного контакта
    contact.id = new_contacts[len(new_contacts)-1].id
    old_contacts.append(contact)

    assert sorted(old_contacts, key=Contact.id_or_max) == new_contacts
    if check_ui:
        app_contacts = app.contacts.get_contacts_list()
        for new_contact in new_contacts:
            for app_contact in app_contacts:
                if new_contact.id == app_contact.id:
                    assert new_contact.firstname == app_contact.firstname
                    break
