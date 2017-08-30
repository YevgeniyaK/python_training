from model.contact import Contact
from random import randrange

def test_change_contact(app):
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

    contact = Contact(firstname="Updated", lastname="Updated")
    old_contacts = app.contacts.get_contacts_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contacts.change_contact(index, Contact(firstname="Updated", middlename="Updated", lastname="Updated",
                                               nickname="Nick", title="Mrs", company="Company_changed", address="Address",
                                               phone_home="+74951234567", phone_mobile="+79031234567",
                                               phone_work="+74961234567",
                                               fax_number="+74961234560", email="test@mail.ru", email2="upd@mail.ru", email3="upd3@gmail.com",
                                               homepage="http://example.com", birthday_day="21", birthday_month="12",
                                               birthday_year="1990", anniversary_day="18", anniversary_month="10",
                                               anniversary_year="2010", secondary_address="secondary address",
                                               secondary_phone="(333)1234567", notes="notes"))
    new_contacts = app.contacts.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
