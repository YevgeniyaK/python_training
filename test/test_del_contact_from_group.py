from model.contact import Contact
from model.group import Group
import random

def test_del_contact_from_group(app, db):
    app_groups = app.group.get_group_list()
    app_contacts = []
    selected_group = None
    for app_group in app_groups:
        app_contacts = app.contacts.get_contacts_list_from_groups_page(app_group.id)
        if len(app_contacts) > 0:
            selected_group = app_group
            break

    # проверяем, что в группе есть контакты
    assert len(app_contacts) > 0
    assert selected_group is not None

    contact_in_group = random.choice(app_contacts)
    app.contacts.delete_contact_from_group_by_id(contact_in_group.id)

    assert db.contact_in_group(contact_in_group.id, selected_group.id) is False

