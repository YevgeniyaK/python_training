from model.contact import Contact

def test_change_contact(app):
    app.session.login(username="admin", password="secret")
    app.contacts.change_contact(Contact(firstname="Updated", middlename="Updated", lastname="Updated",
                         nickname="Nick", title="Mrs", company="Company_changed", address="Address",
                         phone_home="+74951234567", phone_mobile="+79031234567", phone_work="+74961234567",
                         fax_number="+74961234560", email="test@mail.ru",
                         homepage="http://example.com", birthday_day="21", birthday_month="12",
                         birthday_year="1990", anniversary_day="18", anniversary_month="10",
                         anniversary_year="2010", secondary_address="secondary address",
                         home_address="home address", notes="notes"))
    app.session.logout()

