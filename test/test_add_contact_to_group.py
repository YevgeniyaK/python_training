from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, db):
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
    if app.group.count() == 0:
        app.group.create(Group(name="Test"))

    contacts_list = app.contacts.get_contacts_list()
    groups_list = app.group.get_group_list()
    not_empty_groups = []
    for app_group in groups_list:
        if len(app_group.name) > 0:
               not_empty_groups.append(app_group)
    if len(not_empty_groups) == 0:
            created_group = Group(name="Test")
            app.group.create(created_group)
            not_empty_groups.append(created_group)

    random_group = random.choice(not_empty_groups)
    random_contact = random.choice(contacts_list)


    app.contacts.add_contact_to_group(random_contact, random_group)

    assert db.contact_in_group(random_contact.id, random_group.id) is True


