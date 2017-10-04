# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    with pytest.allure.step("Given a contact list"):
        old_contacts = db.get_contact_list()
    with pytest.allure.step("Create a new contact"):
        app.contacts.add_new_contact(contact)
    with pytest.allure.step("Get contact list again"):
        new_contacts = db.get_contact_list()
        new_contacts = sorted(new_contacts, key=Contact.id_or_max)
    with pytest.allure.step("Compare length of old list with length of new list "):
        assert len(old_contacts) + 1 == len(new_contacts)
    with pytest.allure.step("Then the new contact list is equal to the old list with the added contact"):
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
