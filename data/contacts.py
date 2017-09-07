from model.contact import Contact

testdata = [Contact(firstname=random_string_letters("firstname", 10), middlename=random_string_letters("middlename", 10), lastname=random_string_letters("lastname", 10),
                                             nickname=random_string_letters("nickname", 10), title=random_title(), company=random_string_letters("company", 10),
                                             address=random_string("address", 10),
                                             phone_home=random_string_numbers("+", 10), phone_mobile=random_string_numbers("+", 10),
                                             phone_work=random_string_numbers("+", 10),
                                             fax_number=random_string_numbers("fax", 10), email="test@mail.ru", email2="ya@ya.ru", email3="test@gmail.com",
                                             homepage="http://example.com", birthday_day="21", birthday_month="12",
                                             birthday_year="1990", anniversary_day="18", anniversary_month="10",
                                             anniversary_year="2010", secondary_address="1234567",
                                             secondary_phone=random_string_numbers("+", 10), notes=random_string_letters("notes", 10))
            for i in range(n)]
