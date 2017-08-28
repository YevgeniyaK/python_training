from model.contact import Contact
from random import randrange

def test_delete_some_contact(app):
    if app.contacts.count() == 0:
        app.contacts.add_new_contact(Contact(firstname="Firstname", middlename="Middlename", lastname="Lastname",
                         nickname="Nickname", title="Mr", company="Company", address="Address line",
                         phone_home="+74951234567", phone_mobile="+79031234567", phone_work="+74961234567",
                         fax_number="+74961234560", email="test@mail.ru",
                         homepage="http://example.com", birthday_day="21", birthday_month="12",
                         birthday_year="1990", anniversary_day="18", anniversary_month="10",
                         anniversary_year="2010", secondary_address="secondary address",
                         home_address="home address", notes="notes"))
    old_contacts = app.contacts.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contacts.delete_contact_by_index(index)
    new_contacts = app.contacts.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts [index:index+1] = []
    assert old_contacts == new_contacts
