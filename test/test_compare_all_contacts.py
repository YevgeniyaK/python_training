from model.contact import Contact

def test_compare_all_contacts(app, db):
    app_contacts = app.contacts.get_contacts_list()
    db_contacts = db.get_contact_list_for_homepage()
    assert len(app_contacts) == len(db_contacts)
    assert sorted(app_contacts, key=Contact.id_or_max) == sorted(db_contacts, key=Contact.id_or_max)
