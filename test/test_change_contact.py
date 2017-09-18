from model.contact import Contact
import random


def test_change_contact(app, db, check_ui):
    if app.contacts.count() == 0:
        app.contacts.add_new_contact(Contact(firstname="Firstname", middlename="Middlename", lastname="Lastname",
                                             nickname="Nickname", title="Mr", company="Company", address="Address line, 10317, Walterst.5",
                                             phone_home="+74951234567", phone_mobile="+79031234567",
                                             phone_work="+74961234567",
                                             fax_number="+74961234560", email="test@mail.ru", email2="ya@ya.ru", email3="test@gmail.com",
                                             homepage="http://example.com", birthday_day="21", birthday_month="12",
                                             birthday_year="1990", anniversary_day="18", anniversary_month="10",
                                             anniversary_year="2010", secondary_address="1234567",
                                             secondary_phone="123-123456", notes="notes"))

    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact.firstname = "Updated"
    contact.lastname = "Updated"
    app.contacts.change_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        app_contacts = app.contacts.get_contacts_list()
        for new_contact in new_contacts:
            for app_contact in app_contacts:
                if new_contact.id == app_contact.id:
                    if new_contact.id == contact.id:
                        assert new_contact.firstname == contact.firstname
                    else:
                        assert new_contact.firstname == app_contact.firstname
                    break





    #old_contacts[index] = contact
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
